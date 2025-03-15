from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.name import Name
from api_models.player import Player


class Stats(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    games_played: Optional[int] = 0
    wins: Optional[int | List[Player]] = None
    shutouts: Optional[int | List[Player]] = None
    save_pctg: Optional[float | List[Player]] = 0
    record: Optional[str] = "0-0-0"
    gaa: Optional[float] = Field(0.0, alias="goalsAgainstAvg")
    losses: Optional[int] = 0
    ot_losses: Optional[int] = 0
    shots: Optional[int] = 0
    goals: Optional[int | List[Player]] = None
    winning_goals: Optional[int] = 0
    ot_goals: Optional[int] = 0
    assists: Optional[int | List[Player]] = None
    points: Optional[int | List[Player]] = None
    plus_minus: Optional[int | List[Player]] = 0
    penalty_minutes: Optional[int] = Field(0, alias="pim")
    shooting_pctg: Optional[float] = 0
    decision: Optional[str] = ""
    game_date: Optional[str] = ""
    game_id: Optional[int] = 0
    game_type: Optional[int] = 2
    goals_against: Optional[int] = 0
    opponent_abbrev: Optional[str] = ""
    shots_against: Optional[int] = 0
    team_abbrev: Optional[str] = ""
    team_name: Optional[Name] = None
    season: Optional[int] = 0
    league_abbrev: Optional[str] = ""


