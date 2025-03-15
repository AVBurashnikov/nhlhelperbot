from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.name import Name


class SeasonShortSummary(BaseModel):

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    gaa: Optional[float] = 0.0
    games_played: Optional[int] = 0
    losses: Optional[int] = 0
    ot_losses: Optional[int] = 0
    save_pctg: Optional[float] = 0
    season_id: Optional[int] = 0
    wins: Optional[int] = 0


class Award(BaseModel):
    trophy: Name = None
    seasons: List[SeasonShortSummary]