"""Reglas puras (sin Discord ni red): cuándo saludar, cuándo contestar, idioma, claves filtradas
y límites. Separadas para poder probarlas."""
from __future__ import annotations

import re
import time
from collections import defaultdict, deque
from dataclasses import dataclass

# Claves que nunca deberían aparecer en el servidor.
KEY_PATTERNS = [
    re.compile(r"sk-or-v\d-[A-Za-z0-9]{20,}"),          # OpenRouter
    re.compile(r"\bsk-[A-Za-z0-9_-]{30,}"),             # OpenAI y parecidas
    re.compile(r"\bgsk_[A-Za-z0-9]{30,}"),              # Groq
    re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),           # Google
    re.compile(r"\boauth:[a-z0-9]{25,}\b", re.I),       # token de Twitch
]

_ES_WORDS = re.compile(
    r"\b(hola|gracias|qué|que|cómo|como|por qué|porque|tengo|funciona|ayuda|puedo|quiero|necesito|"
    r"buenas|el|la|los|las|una|vicen|no me|ningún|también|dónde|donde|está|esta)\b|[ñ¿¡áéíóú]", re.I)


def contains_key(text: str) -> bool:
    return any(p.search(text or "") for p in KEY_PATTERNS)


def guess_lang(text: str, role_ids: set[int], role_es: int, role_en: int) -> str | None:
    """'es', 'en' o None si no hay pistas. El rol elegido al entrar manda; si no, el texto."""
    if role_es in role_ids and role_en not in role_ids:
        return "es"
    if role_en in role_ids and role_es not in role_ids:
        return "en"
    hits = len(_ES_WORDS.findall(text or ""))
    words = max(1, len((text or "").split()))
    if hits >= 2 or (hits >= 1 and words <= 4):
        return "es"
    if words >= 3:
        return "en"
    return None


def looks_like_question(text: str) -> bool:
    t = (text or "").strip().lower()
    if "?" in t:
        return True
    starts = ("how ", "what ", "why ", "where ", "when ", "can ", "does ", "do ", "is ", "help",
              "cómo ", "como ", "qué ", "que ", "por qué", "dónde ", "donde ", "cuándo ", "puedo ",
              "se puede", "ayuda", "no me ", "no funciona", "doesn't", "not working")
    return t.startswith(starts)


@dataclass
class Situation:
    """Lo que el bot sabe de un mensaje para decidir."""
    is_dm: bool
    channel_id: int            # el canal (o el foro padre si es un hilo)
    in_thread: bool
    thread_owner_is_author: bool
    mentions_bot: bool
    replies_to_bot: bool
    author_is_staff: bool
    staff_spoke_recently: bool  # alguien del equipo contestó en este hilo hace poco
    bot_spoke_in_thread: bool


def should_answer(s: Situation, setup_help: set[int], bug_reports: set[int], silent: set[int]) -> bool:
    if s.is_dm:
        return True
    if s.channel_id in silent:
        return False
    if s.mentions_bot or s.replies_to_bot:
        return True
    if s.author_is_staff:
        return False
    if s.in_thread and s.channel_id in (setup_help | bug_reports):
        # en soporte contesta al que abrió el hilo, salvo que el equipo ya se haya hecho cargo
        if s.staff_spoke_recently:
            return False
        return s.thread_owner_is_author or s.bot_spoke_in_thread
    return False


class RateLimiter:
    """Tope por usuario y hora, y tope global por día. En memoria (se reinicia al reiniciar)."""

    def __init__(self, per_user_hour: int, per_day: int, clock=time.time) -> None:
        self.per_user_hour, self.per_day, self.clock = per_user_hour, per_day, clock
        self.users: dict[int, deque] = defaultdict(deque)
        self.day_key = None
        self.day_count = 0
        self.warned: set[int] = set()

    def allow(self, user_id: int) -> str:
        """'ok', 'user' (pasado de su tope) o 'global' (tope del día)."""
        now = self.clock()
        day = int(now // 86400)
        if day != self.day_key:
            self.day_key, self.day_count = day, 0
        if self.day_count >= self.per_day:
            return "global"
        q = self.users[user_id]
        while q and now - q[0] > 3600:
            q.popleft()
        if len(q) >= self.per_user_hour:
            return "user"
        q.append(now)
        self.day_count += 1
        self.warned.discard(user_id)
        return "ok"


def trim_reply(text: str, limit: int) -> str:
    text = (text or "").strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    for sep in ("\n\n", "\n", ". ", " "):
        i = cut.rfind(sep)
        if i > limit * 0.6:
            return cut[:i].rstrip() + " …"
    return cut + " …"
