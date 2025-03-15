from typing import Optional, List
from pydantic import BaseModel, Field
from api_models.game_day import GameDay


class ScheduleTeam(BaseModel):
    games_by_date: List[GameDay] = Field(None, alias="gamesByDate")
