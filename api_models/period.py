from typing import Optional
from pydantic import BaseModel, Field


class Period(BaseModel):
    """
    Класс, представляющий описание периода игры.

    Атрибуты:
    ----------
    number : Optional[int]
        Номер периода (например, 1, 2, 3 и т.д.). Может быть `None`, если номер не указан.

    period_type : Optional[str]
        Тип периода (например, "REG", "OT", "SO").
        Может быть `None`, если тип не указан.
        Использует псевдоним "periodType" для сериализации/десериализации.
    """

    number: Optional[int] = None
    period_type: Optional[str] = Field(None, alias="periodType")