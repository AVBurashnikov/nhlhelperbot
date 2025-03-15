from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_snake, to_camel

from api_models.name import Name
from api_models.assist import Assist


class Goal(BaseModel):

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    strength: Optional[str] = ""
    player_id: Optional[int]
    name: Optional[Name] = None
    team_abbrev: Optional[str | Name]
    goals_to_date: Optional[int]
    away_score: Optional[int]
    home_score: Optional[int]
    time_in_period: Optional[str]
    assists: Optional[List[Assist]] = None
    period: Optional[int] = 0
    scorer: Optional[Name] = Field(None, alias="name")
    goal_modifier: Optional[str]
