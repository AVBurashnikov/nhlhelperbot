from pydantic import BaseModel, Field

from api_models.player import Player


class Leader(BaseModel):
    category: str = ""
    away_leader: Player = Field(..., alias="awayLeader")
    home_leader: Player = Field(..., alias="homeLeader")
