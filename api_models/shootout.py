from typing import Optional
from pydantic import BaseModel, Field


class Shootout(BaseModel):
    sequence: Optional[int] = 0
    player_id: Optional[int] = Field(0, alias="playerId")
    team_abbrev: Optional[str] = Field("", alias='teamAbbrev')
    first_name: Optional[str] = Field("", alias="firstName")
    last_name: Optional[str] = Field("", alias="lastName")
    result: Optional[str] = ""
    game_winner: Optional[bool] = Field(False, alias="gameWinner")
