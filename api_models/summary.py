from typing import Optional

from pydantic import BaseModel, Field

from api_models.matchup import MatchUp
from api_models.team import Team
from api_models.match_info import MatchInfo


class Summary(BaseModel):
    game_id: Optional[int] = Field(0, alias="id")
    season: Optional[int] = 0
    game_type: Optional[int] = Field(0, alias="gameType")
    start_time: Optional[str] = Field("", alias="startTimeUTC")
    date: Optional[str] = Field("", alias="gameDate")
    game_state: Optional[str] = Field("", alias="gameState")
    away_team: Optional[Team] = Field(None, alias="awayTeam")
    home_team: Optional[Team] = Field(None, alias="homeTeam")
    matchup: Optional[MatchUp] = None
    summary: Optional[MatchInfo] = None
