from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.matchup_leader import Leader


class MatchUpTeamLeaders(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )
    category: str
    away_leader: Leader = None
    home_leader: Leader = None
