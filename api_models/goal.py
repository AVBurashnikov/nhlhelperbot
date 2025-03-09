from typing import List, Optional
from pydantic import BaseModel, Field
from api_models.name import Name
from api_models.assist import Assist


class Goal(BaseModel):
    strength: Optional[str] = ""
    player_id: Optional[int] = Field(0, alias="playerId")
    name: Optional[Name] = None
    team_abbrev: Optional[str | Name] = Field("", alias="teamAbbrev")
    goals_to_date: Optional[int] = Field(0, alias="goalsToDate")
    away_score: Optional[int] = Field(0, alias="awayScore")
    home_score: Optional[int] = Field(0, alias="homeScore")
    time_in_period: Optional[str] = Field("", alias="timeInPeriod")
    assists: Optional[List[Assist]] = None
    period: Optional[int] = 0
    scorer: Optional[Name] = Field(None, alias="name")
    goal_modifier: Optional[str] = Field("", alias="goalModifier")
