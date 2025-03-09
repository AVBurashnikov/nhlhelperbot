from typing import List, Optional
from pydantic import BaseModel, Field
from api_models.game import Game
from api_models.goal import Goal
from api_models.period import Period


class Score(BaseModel):
    current_date: Optional[str] = Field("", alias="currentDate")
    games: Optional[List[Game]] = None
    period_descr: Optional[Period] = Field(None, alias="periodDescriptor")
    goals: Optional[List[Goal]] = None
