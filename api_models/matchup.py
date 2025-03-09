from pydantic import BaseModel, Field

from api_models.player_comparison import GoalieComparison, SkaterComparison


class MatchUp(BaseModel):
    game_type: int = Field(..., alias="gameType")
    skater_comparison: SkaterComparison = Field(..., alias="skaterComparison")
    goalie_comparison: GoalieComparison = Field(..., alias="goalieComparison")

