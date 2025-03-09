from typing import Optional
from pydantic import BaseModel, Field
from api_models.name import Name


class Star(BaseModel):
    star_order: Optional[int] = Field(0, alias="star")
    player_id: Optional[int] = Field("", alias="playerId")
    team_abbrev: Optional[str] = Field("", alias="teamAbbrev")
    name: Optional[Name] = Field(None, description="Player name")
    position: Optional[str] = ""
    save_pctg: Optional[float] = Field(0, alias="savePctg")
    goals: Optional[int] = 0
    assists: Optional[int] = 0
