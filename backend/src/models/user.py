from pydantic import BaseModel
from typing import Optional
from enum import StrEnum


class UserStatus(StrEnum):
    Active = "Active"
    Stale = "Stale"
    DeActive = "DeActive"


class UserCreate(BaseModel):
    first_name: str
    Last_name: str
    email: Optional[str]
    password: str
    status: UserStatus
