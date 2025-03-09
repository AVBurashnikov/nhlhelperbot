from typing import List, Optional

from pydantic import BaseModel, Field

from api_models.game_day import GameDay


class Schedule(BaseModel):
    game_week: Optional[List[GameDay]] = Field(None, alias="gameWeek")
