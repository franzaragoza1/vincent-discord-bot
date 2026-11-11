"""Recorre on_message con objetos de Discord simulados y un cerebro falso."""
import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import discord

from vincentbot.config import Config
from vincentbot.main import VincentBot

BOT_ID = 999
GENERAL = 1569612975927599126
SETUP = 1569619571470504117
ROLE_ES = 1569617664542904320
TEAM = 1569616990165803093


class Hist:
    def __init__(self, msgs): self.msgs = msgs
    def __aiter__(self):
        async def gen():
            for m in reversed(self.msgs):
                yield m
        return gen()


def make_bot(tmp_path):
    cfg = Config(); cfg.db_path = str(tmp_path / "b.db"); cfg.gcp_project = ""; cfg.groq_api_key = "x"
    bot = VincentBot.__new__(VincentBot)
    bot.cfg = cfg
    from vincentbot.store import Store
    from vincentbot.rules import RateLimiter
    bot.store = Store(cfg.db_path); bot.limits = RateLimiter(15, 600); bot.locks = {}
    bot.brain = SimpleNamespace(reply=AsyncMock(return_value="Copy. Check Settings → Audio."))
    bot._connection = SimpleNamespace(user=SimpleNamespace(id=BOT_ID))
    type(bot).user = property(lambda self: SimpleNamespace(id=BOT_ID, mention=f"<@{BOT_ID}>"))
    return bot


def member(uid, roles=()):
    return SimpleNamespace(id=uid, bot=False, display_name=f"u{uid}", mention=f"<@{uid}>",
                           roles=[SimpleNamespace(id=r) for r in roles], guild=SimpleNamespace(owner_id=1))


def message(author, content, channel, mentions=()):
    m = MagicMock()
    m.author = author; m.content = content; m.channel = channel; m.attachments = []
    m.guild = SimpleNamespace(id=1569612974660911147)
    m.mentions = list(mentions); m.role_mentions = []; m.reference = None
    m.reply = AsyncMock(); m.delete = AsyncMock()
    return m


def text_channel(cid, hist=()):
    ch = MagicMock(spec=discord.TextChannel); ch.id = cid
    ch.history = MagicMock(return_value=Hist(list(hist)))
    ch.typing = MagicMock(return_value=AsyncMock()); ch.send = AsyncMock()
    return ch


def thread(parent, owner, hist=()):
    th = MagicMock(spec=discord.Thread); th.id = 12345; th.parent_id = parent; th.owner_id = owner; th.name = "Mic not working"
    th.history = MagicMock(return_value=Hist(list(hist)))
    th.typing = MagicMock(return_value=AsyncMock()); th.send = AsyncMock()
    return th


def run(c): return asyncio.get_event_loop().run_until_complete(c) if False else asyncio.run(c)


def test_first_message_gets_welcome_only(tmp_path):
    bot = make_bot(tmp_path); u = member(10)
    msg = message(u, "hi all, nice server", text_channel(GENERAL))
    run(bot.on_message(msg))
    assert msg.reply.await_count == 1
    assert "Radio check" in msg.reply.await_args.args[0]
    bot.brain.reply.assert_not_awaited()
    msg2 = message(u, "hello again", text_channel(GENERAL))
    run(bot.on_message(msg2))
    msg2.reply.assert_not_awaited()


def test_first_message_question_gets_welcome_and_answer_in_spanish(tmp_path):
    bot = make_bot(tmp_path); u = member(11, [ROLE_ES])
    msg = message(u, "¿cómo configuro el botón del volante?", text_channel(GENERAL))
    run(bot.on_message(msg))
    assert msg.reply.await_count == 2
    assert "Soy **Vicen**" in msg.reply.await_args_list[0].args[0]
    bot.brain.reply.assert_awaited_once()


def test_setup_help_post_answered_and_staff_not_welcomed(tmp_path):
    bot = make_bot(tmp_path)
    staff = member(1, [TEAM])
    m0 = message(staff, "testing", text_channel(GENERAL))
    run(bot.on_message(m0)); m0.reply.assert_not_awaited()
    u = member(12)
    th = thread(SETUP, owner=12)
    msg = message(u, "My mic isn't detected", th)
    bot.store.mark_welcomed(12)
    run(bot.on_message(msg))
    bot.brain.reply.assert_awaited_once()
    turns = bot.brain.reply.await_args.args[0]
    assert turns[0] == ("user", "[Post title: Mic not working]")
    assert turns[-1] == ("user", "u12: My mic isn't detected")


def test_key_leak_deleted(tmp_path):
    bot = make_bot(tmp_path); u = member(13)
    ch = text_channel(GENERAL)
    msg = message(u, "is this ok sk-or-v1-" + "b" * 64, ch)
    run(bot.on_message(msg))
    msg.delete.assert_awaited_once(); ch.send.assert_awaited_once()
    bot.brain.reply.assert_not_awaited()


def test_mention_in_general(tmp_path):
    bot = make_bot(tmp_path); u = member(14); bot.store.mark_welcomed(14)
    me = bot.user
    msg = message(u, f"<@{BOT_ID}> what model do you recommend?", text_channel(GENERAL), mentions=[me])
    run(bot.on_message(msg))
    bot.brain.reply.assert_awaited_once()
    assert bot.brain.reply.await_args.args[0][-1][1].startswith("u14: Vincent what model")
