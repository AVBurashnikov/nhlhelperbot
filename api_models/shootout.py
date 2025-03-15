from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.name import Name


class Shootout(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    sequence: Optional[int] = 0
    player_id: Optional[int] = 0
    team_abbrev: Optional[Name] = None
    first_name: Optional[Name] = None
    last_name: Optional[Name] = None
    result: Optional[str] = ""
    game_winner: Optional[bool] = False
