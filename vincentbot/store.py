"""Memoria del bot en disco: a quién ha saludado ya (para que la bienvenida salga una sola vez)."""
from __future__ import annotations

import sqlite3
import time


class Store:
    def __init__(self, path: str) -> None:
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE IF NOT EXISTS welcomed (user_id INTEGER PRIMARY KEY, at REAL)")
        self.db.execute("CREATE TABLE IF NOT EXISTS usage (day TEXT PRIMARY KEY, replies INTEGER)")
        self.db.commit()

    def welcomed(self, user_id: int) -> bool:
        return self.db.execute("SELECT 1 FROM welcomed WHERE user_id=?", (user_id,)).fetchone() is not None

    def mark_welcomed(self, user_id: int) -> bool:
        """True si es la primera vez (y lo apunta)."""
        cur = self.db.execute("INSERT OR IGNORE INTO welcomed VALUES (?, ?)", (user_id, time.time()))
        self.db.commit()
        return cur.rowcount == 1

    def count_reply(self) -> None:
        day = time.strftime("%Y-%m-%d")
        self.db.execute("INSERT INTO usage VALUES (?, 1) ON CONFLICT(day) DO UPDATE SET replies=replies+1", (day,))
        self.db.commit()
