"""Configuración del bot. Todo sale de variables de entorno (en la nube, de Secret Manager)."""
from __future__ import annotations

import os
from dataclasses import dataclass, field


def _ids(name: str, default: str) -> set[int]:
    raw = os.getenv(name, default)
    return {int(x) for x in raw.replace(" ", "").split(",") if x}


@dataclass
class Config:
    discord_token: str = field(default_factory=lambda: os.getenv("DISCORD_TOKEN", ""))
    guild_id: int = field(default_factory=lambda: int(os.getenv("GUILD_ID", "1569612974660911147")))

    # --- cerebro ---
    # Gemini en Vertex AI (se paga con los créditos de Google Cloud). Se prueban en orden y se queda
    # con el primero que responda: así no se rompe cuando Google retire un modelo antiguo.
    gcp_project: str = field(default_factory=lambda: os.getenv("GCP_PROJECT", ""))
    gcp_location: str = field(default_factory=lambda: os.getenv("GCP_LOCATION", "global"))
    gemini_models: list[str] = field(default_factory=lambda: [m.strip() for m in os.getenv(
        "GEMINI_MODELS", "gemini-3.8-flash,gemini-3.8-flash-preview,gemini-3.5-flash,gemini-3.5-flash-preview,gemini-3-flash,gemini-flash-latest,gemini-2.5-flash").split(",") if m.strip()])
    # Respaldo gratis (opcional): Groq, API compatible con OpenAI.
    groq_api_key: str = field(default_factory=lambda: os.getenv("GROQ_API_KEY", ""))
    groq_model: str = field(default_factory=lambda: os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"))

    # --- canales y roles del servidor de VINCENT ---
    setup_help: set[int] = field(default_factory=lambda: _ids("CH_SETUP_HELP", "1569619571470504117"))
    bug_reports: set[int] = field(default_factory=lambda: _ids("CH_BUG_REPORTS", "1569619713787428864"))
    # canales donde nunca habla
    silent: set[int] = field(default_factory=lambda: _ids(
        "CH_SILENT", "1569619174362325054,1569619300464070746,1569618343151927346,"
                     "1569618419458769026,1569618545770500207,1569618671503151195,1569619803633618964"))
    staff_roles: set[int] = field(default_factory=lambda: _ids("ROLE_STAFF", "1569616990165803093,1569617035263217704"))
    role_es: int = field(default_factory=lambda: int(os.getenv("ROLE_ES", "1569617664542904320")))
    role_en: int = field(default_factory=lambda: int(os.getenv("ROLE_EN", "1569617538495815730")))
    logs_channel: int = field(default_factory=lambda: int(os.getenv("CH_LOGS", "1569619300464070746")))

    # --- límites de gasto ---
    per_user_per_hour: int = field(default_factory=lambda: int(os.getenv("LIMIT_USER_HOUR", "15")))
    global_per_day: int = field(default_factory=lambda: int(os.getenv("LIMIT_DAY", "600")))
    history_messages: int = field(default_factory=lambda: int(os.getenv("HISTORY", "12")))
    max_reply_chars: int = 1900

    db_path: str = field(default_factory=lambda: os.getenv("DB_PATH", "vincentbot.sqlite3"))
