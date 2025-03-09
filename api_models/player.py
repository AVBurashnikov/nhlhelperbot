from typing import Optional
from pydantic import BaseModel, Field
from api_models.name import Name


class Player(BaseModel):
    player_id: Optional[int] = Field(0, alias="id")
    leader_id: Optional[int] = Field(0, alias="playerId")
    first_name: Optional[Name] = Field(None, alias="firstName")
    last_name: Optional[Name] = Field(None, alias="lastName")
    name: Optional[Name] = None
    sweater_number: Optional[int] = Field(0, alias="sweaterNumber")
    birth_country: Optional[str] = Field("", alias="birthCountry")
    position: Optional[str] = ""
    position_code: Optional[str] = Field(None, alias="positionCode", description="Position for matchup entity.")
    team_abbrev: Optional[str] = Field("", alias="teamAbbrev")
    value: Optional[int|float] = 0
