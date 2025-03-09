from typing import List, Optional
from pydantic import BaseModel, Field
from api_models.team import Team


class Standing(BaseModel):
    teams: Optional[List[Team]] = Field(None, alias="standings")

