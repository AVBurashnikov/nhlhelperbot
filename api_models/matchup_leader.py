from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.player import Player


class Leader(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    category: str = ""
    away_leader: Player = None
    home_leader: Player = None
