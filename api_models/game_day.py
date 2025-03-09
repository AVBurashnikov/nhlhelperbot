from typing import List, Optional

from pydantic import BaseModel

from api_models.game import Game


class GameDay(BaseModel):
    date: Optional[str] = ""
    games: Optional[List[Game]] = None
