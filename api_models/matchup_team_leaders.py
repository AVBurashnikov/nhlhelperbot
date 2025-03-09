from pydantic import BaseModel, Field

from api_models.matchup_leader import Leader


class MatchUpTeamLeaders(BaseModel):
    category: str
    away_leader: Leader = Field(..., alias="awayLeader")
    home_leader: Leader = Field(..., alias="homeLeader")
