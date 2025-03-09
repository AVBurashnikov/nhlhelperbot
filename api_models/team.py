from typing import Optional, List

from pydantic import BaseModel, Field

from api_models.name import Name
from api_models.player_extended import PlayerExtended
from api_models.stats import Stats


class Team(BaseModel):
    team_id: int = Field(0, alias="id")
    conference_abbrev: Optional[str] = Field("", alias="conferenceAbbrev")
    division_abbrev: Optional[str] = Field("", alias="divisionAbbrev")
    abbrev: Optional[str | Name] = None
    team_abbrev: Optional[str | Name] = Field(None, alias="teamAbbrev")
    score: Optional[int] = 0
    sog: Optional[int] = 0
    record: Optional[str] = ""
    common_name: Optional[Name] = Field(None, alias="commonName")
    place_name: Optional[Name] = Field(None, alias="placeName")
    name: Optional[Name] = None
    games_played: Optional[int] = Field(0, alias="gamesPlayed")
    points: Optional[int] = 0
    wins: Optional[int] = 0
    losses: Optional[int] = 0
    ot_losses: Optional[int] = Field(0, alias="otLosses")
    team_name: Optional[Name] = Field(None, alias="teamName")
    goalie_total_stats: Optional[Stats] = Field(None, alias="teamTotals")
    leaders: Optional[List[PlayerExtended]] = None
