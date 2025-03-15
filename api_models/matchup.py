from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.player_comparison import GoalieComparison, SkaterComparison


class MatchUp(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    game_type: int = 0
    skater_comparison: SkaterComparison = None
    goalie_comparison: GoalieComparison = None

