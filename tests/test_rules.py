from vincentbot.config import Config
from vincentbot.llm import _merge
from vincentbot.rules import RateLimiter, Situation, contains_key, guess_lang, looks_like_question, should_answer, trim_reply
from vincentbot.store import Store
from vincentbot import texts

C = Config()
SETUP = next(iter(C.setup_help)); BUGS = next(iter(C.bug_reports))
GENERAL = 1569612975927599126; WELCOME_CH = 1569618343151927346


def sit(**kw):
    base = dict(is_dm=False, channel_id=GENERAL, in_thread=False, thread_owner_is_author=False, mentions_bot=False,
                replies_to_bot=False, author_is_staff=False, staff_spoke_recently=False, bot_spoke_in_thread=False)
    base.update(kw)
    return Situation(**base)


def ans(s):
    return should_answer(s, C.setup_help, C.bug_reports, C.silent)


def test_general_only_when_called():
    assert not ans(sit())
    assert ans(sit(mentions_bot=True))
    assert ans(sit(replies_to_bot=True))


def test_dm_always():
    assert ans(sit(is_dm=True))


def test_silent_channels_never_even_if_mentioned():
    assert not ans(sit(channel_id=WELCOME_CH, mentions_bot=True))


def test_setup_help_thread_owner():
    assert ans(sit(channel_id=SETUP, in_thread=True, thread_owner_is_author=True))
    assert not ans(sit(channel_id=SETUP, in_thread=True, thread_owner_is_author=False))
    assert ans(sit(channel_id=SETUP, in_thread=True, bot_spoke_in_thread=True))


def test_staff_takes_over():
    assert not ans(sit(channel_id=SETUP, in_thread=True, thread_owner_is_author=True, staff_spoke_recently=True))
    assert not ans(sit(channel_id=SETUP, in_thread=True, author_is_staff=True))
    assert ans(sit(channel_id=SETUP, in_thread=True, author_is_staff=True, mentions_bot=True))


def test_bug_reports_thread():
    assert ans(sit(channel_id=BUGS, in_thread=True, thread_owner_is_author=True))


def test_keys():
    assert contains_key("my key sk-or-v1-" + "a" * 64)
    assert contains_key("gsk_" + "A1" * 20)
    assert not contains_key("my fuel is 38 litres sk8 board")


def test_lang():
    assert guess_lang("hello", {C.role_es}, C.role_es, C.role_en) == "es"
    assert guess_lang("hola", {C.role_en}, C.role_es, C.role_en) == "en"
    assert guess_lang("hola, no me funciona el micro", set(), C.role_es, C.role_en) == "es"
    assert guess_lang("my wheel button is not detected", set(), C.role_es, C.role_en) == "en"
    assert guess_lang("hi", set(), C.role_es, C.role_en) is None


def test_question():
    assert looks_like_question("how do I set the wheel button")
    assert looks_like_question("no me funciona el micro")
    assert looks_like_question("anyone?")
    assert not looks_like_question("hi all, nice server")


def test_rate_limit():
    t = [0.0]
    rl = RateLimiter(2, 3, clock=lambda: t[0])
    assert rl.allow(1) == "ok" and rl.allow(1) == "ok"
    assert rl.allow(1) == "user"
    assert rl.allow(2) == "ok"
    assert rl.allow(3) == "global"
    t[0] = 86400 + 4000
    assert rl.allow(1) == "ok"


def test_store_welcome_once(tmp_path):
    s = Store(str(tmp_path / "x.db"))
    assert s.mark_welcomed(5) is True
    assert s.mark_welcomed(5) is False


def test_merge_alternates_and_starts_with_user():
    out = _merge([("model", "a"), ("user", "b"), ("user", "c"), ("model", "d")])
    assert out == [("user", "b\nc"), ("model", "d")]


def test_trim():
    assert trim_reply("x" * 10, 20) == "x" * 10
    assert len(trim_reply("word " * 1000, 1900)) <= 1905


def test_welcome_texts_fit():
    for k, v in texts.WELCOME.items():
        assert len(v.format(name="Someone With A Long Name")) < 2000, k
