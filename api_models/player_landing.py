from typing import Optional, List
from pydantic import Field

from api_models.award import Award
from api_models.player import Player
from api_models.name import Name
from api_models.player_stats import PlayerStats
from api_models.stats import Stats


class PlayerLanding(Player):
    current_team_abbrev: Optional[str] = Field("", alias="currentTeamAbbrev")
    full_team_name: Optional[Name] = Field(None, alias="fullTeamName")
    position: Optional[str] = ""
    height: Optional[int] = Field(0, alias="heightInCentimeters")
    weight: Optional[int] = Field(0, alias="weightInKilograms")
    birth_date: Optional[str] = Field("", alias="birthDate")
    featured_stats: Optional[PlayerStats] = Field(None,
                                                    alias="featuredStats",
                                                    description="Функциональная статистика игрока")
    last_5_games: Optional[List[Stats]] = Field(None, alias="last5Games")
    season_totals: Optional[List[Stats]] = Field(None, alias="seasonTotals")
    awards: Optional[List[Award]] = None
