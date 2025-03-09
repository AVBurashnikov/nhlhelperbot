from typing import Optional
from pydantic import BaseModel, Field
from api_models.name import Name


class PenaltyInfo(BaseModel):
    """
    Класс, представляющий информацию о нарушении в игре.

    Атрибуты:
    ----------
    time_in_period : Optional[str]
        Время в периоде, когда был назначен штраф. Может быть `None`, если время не указано.
        Использует псевдоним "timeInPeriod" для сериализации/десериализации.

    penalty_type : Optional[str]
        Тип штрафа. Может быть `None`, если тип не указан.
        Использует псевдоним "type" для сериализации/десериализации.

    duration : Optional[int]
        Длительность штрафа в секундах. Может быть `None`, если длительность не указана.

    player_name : Optional[str]
        Имя игрока, нарушившего правила. Может быть `None`, если имя не указано.
        Использует псевдоним "committedByPlayer" для сериализации/десериализации.

    team_abbrev : Optional[Name]
        Аббревиатура команды, к которой принадлежит игрок. Обязательное поле.
        Использует псевдоним "teamAbbrev" для сериализации/десериализации.

    description : Optional[str]
        Описание штрафа. Может быть `None`, если описание не указано.
        Использует псевдоним "descKey" для сериализации/десериализации.

    served_by : Optional[str]
        Имя игрока, отбывающего штраф. Может быть `None`, если имя не указано.
        Использует псевдоним "servedBy" для сериализации/десериализации.
    """

    time_in_period: Optional[str] = Field(None, alias="timeInPeriod")
    penalty_type: Optional[str] = Field(None, alias="type")
    duration: Optional[int]
    player_name: Optional[Name] = Field(None, alias="committedByPlayer")
    team_abbrev: Optional[Name] = Field(..., alias="teamAbbrev")
    description: Optional[str] = Field(None, alias="descKey")
    served_by: Optional[Name] = Field(None, alias="servedBy")
