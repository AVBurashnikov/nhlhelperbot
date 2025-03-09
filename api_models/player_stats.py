from typing import Optional

from pydantic import BaseModel, Field

from api_models.player_stats_by_season import PlayerStatsBySeason


class PlayerStats(BaseModel):
    season: Optional[int] = 0
    regular_season: Optional[PlayerStatsBySeason] = Field(None, alias="regularSeason")