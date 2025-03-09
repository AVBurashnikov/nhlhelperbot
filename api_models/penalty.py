from typing import List, Optional
from pydantic import BaseModel, Field
from api_models.penalty_info import PenaltyInfo
from api_models.period import Period


class Penalty(BaseModel):
    """
    Класс, представляющий информацию о штрафах в конкретном периоде игры.

    Атрибуты:
    ----------
    period_descr : Optional[Period]
        Описание периода игры (например, номер периода, тип периода).
        Может быть `None`, если описание не указано.
        Использует псевдоним "periodDescriptor" для сериализации/десериализации.

    penalties : Optional[List[PenaltyInfo]]
        Список объектов `PenaltyInfo`, содержащих информацию о штрафах в этом периоде.
        Может быть `None`, если список штрафов пуст или не указан.
    """

    period_descr: Optional[Period] = Field(None, alias="periodDescriptor")
    penalties: Optional[List[PenaltyInfo]]