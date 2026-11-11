"""El cerebro: Gemini en Vertex AI (créditos de Google Cloud) con Groq gratis de respaldo."""
from __future__ import annotations

import asyncio
import logging

from .config import Config
from .prompt import SYSTEM

log = logging.getLogger("vincentbot.llm")


class Brain:
    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.gemini = None
        self.model: str | None = None
        self.groq = None
        if cfg.gcp_project:
            from google import genai
            self.gemini = genai.Client(vertexai=True, project=cfg.gcp_project, location=cfg.gcp_location)
        if cfg.groq_api_key:
            from openai import AsyncOpenAI
            self.groq = AsyncOpenAI(api_key=cfg.groq_api_key, base_url="https://api.groq.com/openai/v1")

    async def pick_model(self) -> None:
        """Prueba los modelos de Gemini en orden y se queda con el primero que funcione."""
        if not self.gemini:
            return
        for m in self.cfg.gemini_models:
            try:
                r = await asyncio.wait_for(self.gemini.aio.models.generate_content(model=m, contents="ping"), 30)
                if r.text is not None:
                    self.model = m
                    log.info("Gemini model: %s", m)
                    return
            except Exception as e:  # modelo inexistente o sin acceso en este proyecto
                log.warning("Model %s unavailable: %s", m, str(e)[:160])
        log.error("No Gemini model available; will use Groq if configured")

    async def reply(self, history: list[tuple[str, str]]) -> str:
        """history: [(role, text)] con role 'user' o 'model', el último es el mensaje a contestar."""
        if self.gemini and self.model:
            try:
                return await asyncio.wait_for(self._gemini(history), 45)
            except Exception as e:
                log.warning("Gemini failed: %s", str(e)[:200])
        if self.groq:
            return await asyncio.wait_for(self._groq(history), 45)
        raise RuntimeError("no brain available")

    async def _gemini(self, history):
        from google.genai import types
        contents = [types.Content(role=r, parts=[types.Part(text=t)]) for r, t in _merge(history)]
        r = await self.gemini.aio.models.generate_content(
            model=self.model, contents=contents,
            config=types.GenerateContentConfig(system_instruction=SYSTEM, temperature=0.7,
                                               max_output_tokens=700))
        return (r.text or "").strip()

    async def _groq(self, history):
        msgs = [{"role": "system", "content": SYSTEM}]
        msgs += [{"role": "assistant" if r == "model" else "user", "content": t} for r, t in _merge(history)]
        r = await self.groq.chat.completions.create(model=self.cfg.groq_model, messages=msgs,
                                                    temperature=0.7, max_tokens=700)
        return (r.choices[0].message.content or "").strip()


def _merge(history: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Junta turnos seguidos del mismo rol (Gemini exige alternar) y empieza por 'user'."""
    out: list[list] = []
    for role, text in history:
        if out and out[-1][0] == role:
            out[-1][1] += "\n" + text
        else:
            out.append([role, text])
    while out and out[0][0] != "user":
        out.pop(0)
    return [(r, t) for r, t in out]
