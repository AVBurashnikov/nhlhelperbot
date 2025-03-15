from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.name import Name


class Player(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )
    player_id: Optional[int] = Field(0, alias="id")
    leader_id: Optional[int] = Field(0, alias="playerId")
    first_name: Optional[Name] = None
    last_name: Optional[Name] = None
    name: Optional[Name] = None
    sweater_number: Optional[int] = 0
    birth_country: Optional[str] = ""
    position: Optional[str] = ""
    position_code: Optional[str] = Field(None, description="Position for matchup entity.")
    team_abbrev: Optional[str] = ""
    value: Optional[int|float] = 0
