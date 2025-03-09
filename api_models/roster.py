from typing import List, Optional

from pydantic import BaseModel

from api_models.player import Player


class Roster(BaseModel):
    forwards: Optional[List[Player]] = None
    defensemen: Optional[List[Player]] = None
    goalies: Optional[List[Player]] = None
