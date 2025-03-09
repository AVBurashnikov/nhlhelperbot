from typing import Optional, List
from pydantic import BaseModel, Field
from api_models.player import Player


class Stats(BaseModel):
    games_played: Optional[int] = Field(0, alias="gamesPlayed")
    wins: Optional[int | List[Player]] = None
    shutouts: Optional[int | List[Player]] = None
    save_pctg: Optional[float | List[Player]] = Field(None, alias="savePctg")
    record: Optional[str] = ""
    gaa: Optional[float] = Field(0.0, alias="goalsAgainstAvg")
    losses: Optional[int] = 0
    ot_losses: Optional[int] = Field(0, alias="otLosses")
    shots: Optional[int] = 0
    goals: Optional[int | List[Player]] = None
    winning_goals: Optional[int] = Field(0, alias="winningGoals")
    ot_goals: Optional[int] = Field(0, alias="otGoals")
    assists: Optional[int | List[Player]] = None
    points: Optional[int | List[Player]] = None
    plus_minus: Optional[int | List[Player]] = Field(0, alias="plusMinus")
    penalty_minutes: Optional[int] = Field(0, alias="pim")
    shooting_pctg: Optional[float] = Field(0.0, alias="shootingPctg")
    decision: Optional[str] = ""
    game_date: Optional[str] = Field("", alias="gameDate")
    game_id: Optional[int] = Field(0, alias="gameId")
    game_type: Optional[int] = Field(2, alias="gameTypeId")
    goals_against: Optional[int] = Field(0, alias="goalsAgainst")
    opponent_abbrev: Optional[str] = Field("", alias="opponentAbbrev")
    shots_against: Optional[int] = Field(0, alias="shotsAgainst")
    team_abbrev: Optional[str] = Field("", alias="teamAbbrev")


