from typing import List, Optional

from pydantic import BaseModel, Field

from api_models.penalty import Penalty
from api_models.score import Score
from api_models.shootout import Shootout
from api_models.star import Star


class MatchInfo(BaseModel):
    scoring: Optional[List[Score]] = None
    shootout: Optional[List[Shootout]] = None
    three_stars: Optional[List[Star]] = Field(None, alias="threeStars")
    penalties: Optional[List[Penalty]] = None