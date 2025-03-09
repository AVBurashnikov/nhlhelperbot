from typing import Optional, List
from pydantic import BaseModel, Field

from api_models.clock import Clock
from api_models.goal import Goal
from api_models.team import Team


class Game(BaseModel):
    game_id: Optional[int] = Field(0, alias="id")
    game_state: Optional[str] = Field("", alias="gameState")
    start_time_utc: Optional[str] = Field("", alias="startTimeUTC")
    away_team: Optional[Team] = Field(None, alias="awayTeam")
    home_team: Optional[Team] = Field(None, alias="homeTeam")
    three_min_recap: Optional[str] = Field(None, alias="threeMinRecap")
    clock: Optional[Clock] = None
    goals: Optional[List[Goal]] = None
