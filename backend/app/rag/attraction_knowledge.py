"""Small city-attraction retrieval layer for TravelMind."""

import json
from pathlib import Path
from typing import Any


KNOWLEDGE_PATH = Path(__file__).resolve().parent / "city_attractions.json"


class AttractionKnowledgeBase:
    """Keyword retrieval over a compact JSON attraction knowledge base."""

    def __init__(self, path: Path = KNOWLEDGE_PATH):
        self.path = path

    def _load(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def retrieve(self, city: str, preferences: list[str], limit: int = 4) -> list[dict[str, Any]]:
        rows = self._load()
        preference_terms = {term.strip() for term in preferences if term.strip()}
        scored = []

        for row in rows:
            if row.get("city") != city:
                continue
            tags = set(row.get("tags", []))
            score = len(tags & preference_terms)
            if row.get("name") in preference_terms:
                score += 2
            scored.append((score, row))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [row for _, row in scored[:limit]]


_knowledge_base = AttractionKnowledgeBase()


def get_attraction_knowledge_base() -> AttractionKnowledgeBase:
    return _knowledge_base


