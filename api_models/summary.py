from typing import Optional

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.matchup import MatchUp
from api_models.team import Team
from api_models.match_info import MatchInfo


class Summary(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    game_id: Optional[int] = Field(0, alias="id")
    season: Optional[int] = 0
    game_type: Optional[int] = 0
    start_time: Optional[str] = Field("", alias="startTimeUTC")
    date: Optional[str] = Field("", alias="gameDate")
    game_state: Optional[str] = ""
    away_team: Optional[Team] = None
    home_team: Optional[Team] = None
    matchup: Optional[MatchUp] = None
    summary: Optional[MatchInfo] = None
