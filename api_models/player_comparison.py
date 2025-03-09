from typing import List

from pydantic import BaseModel, Field

from api_models.matchup_leader import Leader
from api_models.team import Team


class SkaterComparison(BaseModel):
    context_label: str = Field(..., alias="contextLabel")
    context_season: int = Field(..., alias="contextSeason")
    leaders: List[Leader]


class GoalieComparison(BaseModel):
    context_label: str = Field(..., alias="contextLabel")
    context_season: int = Field(..., alias="contextSeason")
    away_team: Team = Field(..., alias="awayTeam")
    home_team: Team = Field(..., alias="homeTeam")

