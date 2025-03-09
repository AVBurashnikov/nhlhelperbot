from typing import Optional

from pydantic import BaseModel, Field


class Name(BaseModel):
    default: Optional[str] = Field(description="Default localization name")