from typing import Optional, List
from pydantic import Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.award import Award
from api_models.player import Player
from api_models.name import Name
from api_models.player_stats import PlayerStats
from api_models.stats import Stats


class PlayerLanding(Player):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )
    current_team_abbrev: Optional[str] = ""
    full_team_name: Optional[Name] = None
    position: Optional[str] = ""
    height: Optional[int] = Field(0, alias="heightInCentimeters")
    weight: Optional[int] = Field(0, alias="weightInKilograms")
    birth_date: Optional[str] = ""
    featured_stats: Optional[PlayerStats] = Field(None, description="Функциональная статистика игрока")
    last_5_games: Optional[List[Stats]] = Field(None, alias="last5Games")
    season_totals: Optional[List[Stats]] = None
    awards: Optional[List[Award]] = None
