from typing import Optional

from pydantic import BaseModel, Field

from api_models.stats import Stats


class PlayerStatsBySeason(BaseModel):
    current_season: Optional[Stats] = Field(None, alias="subSeason")
    career: Optional[Stats] = None
