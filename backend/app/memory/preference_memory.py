"""Simple JSON-backed preference memory for TravelMind."""

import json
from collections import Counter
from pathlib import Path
from typing import Any

from ..models.schemas import TripPlan, TripRequest


MEMORY_PATH = Path(__file__).resolve().parent / "user_preferences.json"


class PreferenceMemory:
    """Store and recall lightweight user travel preferences."""

    def __init__(self, path: Path = MEMORY_PATH):
        self.path = path

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {}
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}

    def _save(self, data: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def recall(self, user_id: str, city: str) -> str:
        data = self._load()
        profile = data.get(user_id, {})
        trips = profile.get("trips", [])
        preference_counter = Counter(profile.get("preferences", []))
        transport_counter = Counter(profile.get("transportation", []))
        accommodation_counter = Counter(profile.get("accommodation", []))
        city_trips = [trip for trip in trips if trip.get("city") == city]

        hints = []
        if preference_counter:
            top_preferences = "、".join(item for item, _ in preference_counter.most_common(5))
            hints.append(f"历史高频偏好: {top_preferences}")
        if transport_counter:
            hints.append(f"常用交通方式: {transport_counter.most_common(1)[0][0]}")
        if accommodation_counter:
            hints.append(f"常选住宿类型: {accommodation_counter.most_common(1)[0][0]}")
        if city_trips:
            hints.append(f"曾规划过{city}，可避免重复安排过于相似的路线。")

        return "\n".join(hints)

    def remember(self, user_id: str, request: TripRequest, trip_plan: TripPlan) -> None:
        data = self._load()
        profile = data.setdefault(
            user_id,
            {
                "preferences": [],
                "transportation": [],
                "accommodation": [],
                "trips": [],
            },
        )

        profile["preferences"].extend(request.preferences or [])
        profile["transportation"].append(request.transportation)
        profile["accommodation"].append(request.accommodation)
        profile["trips"].append(
            {
                "city": request.city,
                "start_date": request.start_date,
                "end_date": request.end_date,
                "days": request.travel_days,
                "budget": request.budget_constraint.amount,
                "generated_days": len(trip_plan.days),
            }
        )
        profile["trips"] = profile["trips"][-20:]
        self._save(data)


_memory = PreferenceMemory()


def get_preference_memory() -> PreferenceMemory:
    return _memory


