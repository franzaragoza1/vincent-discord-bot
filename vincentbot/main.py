"""Vincent en Discord: saluda siempre igual al primer mensaje de cada persona y contesta dudas
con la guía oficial como conocimiento."""
from __future__ import annotations

import asyncio
import logging
import re

import discord

from . import texts
from .config import Config
from .llm import Brain
from .rules import RateLimiter, Situation, contains_key, guess_lang, looks_like_question, should_answer, trim_reply
from .store import Store

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("vincentbot")


class VincentBot(discord.Client):
    def __init__(self, cfg: Config) -> None:
        intents = discord.Intents.default()
        intents.message_content = True      # hay que activarlo también en el portal de Discord
        super().__init__(intents=intents, allowed_mentions=discord.AllowedMentions(everyone=False, roles=False,
                                                                                    users=True, replied_user=False))
        self.cfg = cfg
        self.brain = Brain(cfg)
        self.store = Store(cfg.db_path)
        self.limits = RateLimiter(cfg.per_user_per_hour, cfg.global_per_day)
        self.locks: dict[int, asyncio.Lock] = {}

    async def setup_hook(self) -> None:
        await self.brain.pick_model()

    async def on_ready(self) -> None:
        log.info("Logged in as %s (model: %s, groq: %s)", self.user, self.brain.model, bool(self.brain.groq))
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the team radio"))

    # ------------------------------------------------------------------ helpers
    def _is_staff(self, member) -> bool:
        roles = {r.id for r in getattr(member, "roles", [])}
        return bool(roles & self.cfg.staff_roles) or getattr(member, "id", 0) == getattr(
            getattr(member, "guild", None), "owner_id", -1)

    def _mentions_me(self, msg: discord.Message) -> bool:
        if self.user in msg.mentions:
            return True
        return any(r.tags and r.tags.bot_id == self.user.id for r in msg.role_mentions)

    async def _replies_to_me(self, msg: discord.Message) -> bool:
        ref = msg.reference
        if not ref or not ref.message_id:
            return False
        target = ref.resolved if isinstance(ref.resolved, discord.Message) else None
        if target is None:
            try:
                target = await msg.channel.fetch_message(ref.message_id)
            except discord.HTTPException:
                return False
        return target.author.id == self.user.id

    def _clean(self, text: str) -> str:
        return re.sub(rf"<@[!&]?{self.user.id}>", "Vincent", text or "").strip()

    def _lang(self, msg: discord.Message) -> str | None:
        roles = {r.id for r in getattr(msg.author, "roles", [])}
        return guess_lang(msg.content, roles, self.cfg.role_es, self.cfg.role_en)

    # ------------------------------------------------------------------ events
    async def on_message(self, msg: discord.Message) -> None:
        if msg.author.bot or not self.user:
            return
        is_dm = msg.guild is None
        if not is_dm and msg.guild.id != self.cfg.guild_id:
            return
        lang = self._lang(msg)

        # 1) claves filtradas: fuera antes que nada
        if not is_dm and contains_key(msg.content):
            await self._handle_key_leak(msg, lang or "en")
            return

        channel = msg.channel
        in_thread = isinstance(channel, discord.Thread)
        parent_id = channel.parent_id if in_thread else channel.id
        staff = not is_dm and self._is_staff(msg.author)

        # 2) bienvenida fija, una sola vez por persona
        first = False
        if not is_dm and not staff and parent_id not in self.cfg.silent:
            if self.store.mark_welcomed(msg.author.id):
                first = True
                text = texts.WELCOME[lang or "both"].format(name=msg.author.display_name)
                try:
                    await msg.reply(text, mention_author=False, suppress_embeds=True)
                except discord.HTTPException as e:
                    log.warning("welcome failed: %s", e)

        # 3) ¿le toca contestar?
        history = await self._history(msg) if (in_thread or is_dm or self._mentions_me(msg)) else []
        sit = Situation(
            is_dm=is_dm, channel_id=parent_id, in_thread=in_thread,
            thread_owner_is_author=in_thread and channel.owner_id == msg.author.id,
            mentions_bot=self._mentions_me(msg), replies_to_bot=await self._replies_to_me(msg),
            author_is_staff=staff,
            staff_spoke_recently=any(m.author.id != self.user.id and self._is_staff(m.author) for m in history[-6:]),
            bot_spoke_in_thread=any(m.author.id == self.user.id for m in history),
        )
        answer = should_answer(sit, self.cfg.setup_help, self.cfg.bug_reports, self.cfg.silent)
        if first and not answer and looks_like_question(msg.content) and parent_id not in self.cfg.silent:
            answer = True
        if not answer:
            return
        await self._answer(msg, history or await self._history(msg), lang or "en")

    async def _history(self, msg: discord.Message) -> list[discord.Message]:
        out = []
        try:
            async for m in msg.channel.history(limit=self.cfg.history_messages, before=msg):
                out.append(m)
        except discord.HTTPException:
            pass
        out.reverse()
        return out

    async def _answer(self, msg: discord.Message, history: list[discord.Message], lang: str) -> None:
        verdict = self.limits.allow(msg.author.id)
        if verdict != "ok":
            if msg.author.id not in self.limits.warned:
                self.limits.warned.add(msg.author.id)
                txt = (texts.LIMIT_USER if verdict == "user" else texts.LIMIT_GLOBAL)[lang]
                await msg.reply(txt, mention_author=False, suppress_embeds=True)
            return
        lock = self.locks.setdefault(msg.channel.id, asyncio.Lock())
        async with lock:
            turns: list[tuple[str, str]] = []
            title = getattr(msg.channel, "name", "") if isinstance(msg.channel, discord.Thread) else ""
            if title:
                turns.append(("user", f"[Post title: {title}]"))
            for m in history + [msg]:
                if not m.content and not m.attachments:
                    continue
                body = self._clean(m.content)
                if m.attachments:
                    body += " [attached: " + ", ".join(a.filename for a in m.attachments) + "]"
                if m.author.id == self.user.id:
                    turns.append(("model", body))
                else:
                    turns.append(("user", f"{m.author.display_name}: {body}"))
            try:
                async with msg.channel.typing():
                    text = await self.brain.reply(turns)
            except Exception as e:
                log.error("brain failed: %s", e)
                await msg.reply(texts.BRAIN_DOWN[lang], mention_author=False, suppress_embeds=True)
                return
            text = trim_reply(text, self.cfg.max_reply_chars)
            if not text:
                return
            if contains_key(text):  # nunca repetir algo con pinta de clave
                return
            self.store.count_reply()
            await msg.reply(text, mention_author=False, suppress_embeds=True)

    async def _handle_key_leak(self, msg: discord.Message, lang: str) -> None:
        try:
            await msg.delete()
            await msg.channel.send(texts.KEY_LEAK[lang].format(mention=msg.author.mention))
            log.info("deleted a message with an API key from %s", msg.author)
        except discord.Forbidden:
            await msg.reply(texts.KEY_LEAK_NODELETE[lang].format(mention=msg.author.mention), mention_author=True)


def main() -> None:
    cfg = Config()
    if not cfg.discord_token:
        raise SystemExit("DISCORD_TOKEN missing")
    if not cfg.gcp_project and not cfg.groq_api_key:
        raise SystemExit("Set GCP_PROJECT (Gemini on Vertex AI) or GROQ_API_KEY")
    VincentBot(cfg).run(cfg.discord_token, log_handler=None)


if __name__ == "__main__":
    main()
