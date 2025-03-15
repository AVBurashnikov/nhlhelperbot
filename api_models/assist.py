from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from api_models.name import Name


class Assist(BaseModel):
    """
    Класс, представляющий информацию о передачах (ассистах) игрока.

    Атрибуты:
    ----------
    player_id : Optional[int]
        Уникальный идентификатор игрока. Может быть `None`, если идентификатор не указан.
        Использует псевдоним "playerId" для сериализации/десериализации.

    name : Optional[Name]
        Объект, содержащий информацию об имени игрока (например, имя и фамилия).
        Может быть `None`, если имя не указано.

    assists_to_date : Optional[int]
        Количество передач (ассистов), сделанных игроком на текущую дату.
        Может быть `None`, если количество передач не указано.
        Использует псевдоним "assistsToDate" для сериализации/десериализации.
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    player_id: Optional[int]
    name: Optional[Name] = None
    assists_to_date: Optional[int]