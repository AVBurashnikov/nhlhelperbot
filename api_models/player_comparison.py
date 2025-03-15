from typing import List

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.matchup_leader import Leader
from api_models.team import Team


class Comparison(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )
    context_label: str = ""
    context_season: int = 0


class SkaterComparison(Comparison):
    leaders: List[Leader]


class GoalieComparison(Comparison):
    away_team: Team
    home_team: Team

