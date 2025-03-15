from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.name import Name
from api_models.player_extended import PlayerExtended
from api_models.stats import Stats


class Team(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    team_id: int = Field(0, alias="id")
    conference_abbrev: Optional[str] = ""
    division_abbrev: Optional[str] = ""
    abbrev: Optional[str | Name] = None
    team_abbrev: Optional[str | Name] = ""
    score: Optional[int] = 0
    sog: Optional[int] = 0
    record: Optional[str] = ""
    common_name: Optional[Name] = None
    place_name: Optional[Name] = None
    name: Optional[Name] = None
    games_played: Optional[int] = 0
    points: Optional[int] = 0
    wins: Optional[int] = 0
    losses: Optional[int] = 0
    ot_losses: Optional[int] = 0
    team_name: Optional[Name] = None
    goalie_total_stats: Optional[Stats] = Field(None, alias="teamTotals")
    leaders: Optional[List[PlayerExtended]] = None
