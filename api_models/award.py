from typing import List, Optional

from pydantic import BaseModel, Field

from api_models.name import Name


class SeasonShortSummary(BaseModel):
    gaa: Optional[float] = 0.0
    games_played: Optional[int] = Field(0, alias="gamesPlayed")
    losses: Optional[int] = 0
    ot_losses: Optional[int] = 0
    save_pctg: Optional[float] = Field(0.0, alias="savePctg")
    season_id: Optional[int] = Field(0, alias="seasonId")
    wins: Optional[int] = 0


class Award(BaseModel):
    trophy: Name = None
    seasons: List[SeasonShortSummary]