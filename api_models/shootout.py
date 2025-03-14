from typing import Optional
from pydantic import BaseModel, Field

from api_models.name import Name


class Shootout(BaseModel):
    sequence: Optional[int] = 0
    player_id: Optional[int] = Field(0, alias="playerId")
    team_abbrev: Optional[Name] = Field("", alias='teamAbbrev')
    first_name: Optional[Name] = Field("", alias="firstName")
    last_name: Optional[Name] = Field("", alias="lastName")
    result: Optional[str] = ""
    game_winner: Optional[bool] = Field(False, alias="gameWinner")
