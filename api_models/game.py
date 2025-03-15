from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.clock import Clock
from api_models.goal import Goal
from api_models.team import Team


class Game(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    game_id: Optional[int] = Field(0, alias="id")
    game_state: Optional[str] = ""
    start_time_utc: Optional[str] = Field("", alias="startTimeUTC")
    away_team: Optional[Team] = None
    home_team: Optional[Team] = None
    three_min_recap: Optional[str] = ""
    clock: Optional[Clock] = None
    goals: Optional[List[Goal]] = None
