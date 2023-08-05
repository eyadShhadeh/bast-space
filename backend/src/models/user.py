from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum


class UserStatus(str, Enum):
    Active = "Active"
    DeActive = "DeActive"
    Deleted = "Deleted"


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Role(str, Enum):
    ADMIN = "ADMIN"
    CLIENT = "CLIENT"
    CUSTOMER = "CUSTOMER"


class UserCreate(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str
    status: UserStatus
    role: Role = Role.CUSTOMER
    gender: Gender
    delivery_area: Optional[str]
    phone: str
    contact_links: List[str]
    created_at: datetime
    updated_at: datetime
