from typing import Optional
from pydantic import BaseModel, Field


class Clock(BaseModel):
    """
    Класс, представляющий информацию о времени на игровых часах.

    Атрибуты:
    ----------
    time_remaining : Optional[str]
        Оставшееся время на игровых часах в формате строки. Может быть `None`, если время не указано.
        Использует псевдоним "timeRemaining" для сериализации/десериализации.
    """

    time_remaining: Optional[str] = Field(None, alias="timeRemaining")