from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.game import Game
from api_models.goal import Goal
from api_models.period import Period


class Score(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    current_date: Optional[str] = ""
    games: Optional[List[Game]] = None
    period_descr: Optional[Period] = Field(None, alias="periodDescriptor")
    goals: Optional[List[Goal]] = None
