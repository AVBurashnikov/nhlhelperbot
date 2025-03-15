from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.name import Name


class Star(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    star_order: Optional[int] = Field(0, alias="star")
    player_id: Optional[int] = 0
    team_abbrev: Optional[str] = ""
    name: Optional[Name] = Field(None, description="Player name")
    position: Optional[str] = ""
    save_pctg: Optional[float] = 0
    goals: Optional[int] = 0
    assists: Optional[int] = 0
