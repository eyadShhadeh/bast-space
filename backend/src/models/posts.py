from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import date, datetime
from backend.src.models.user import Gender


class HealthStatus(str, Enum):
    FULLY_HEALTHY = "FULLY_HEALTHY"
    SHOTS_NEEDED = "SHOTS_NEEDED"
    CONSTANT_CARE = "CONSTANT_CARE"
    URGENT_CASE = "URGENT_CASE"


class Status(str, Enum):
    FOR_ADOPTION = "FOR_ADOPTION"
    ADOPTED = "ADOPTED"
    ESCAPED = "ESCAPED"
    DEAD = "DEAD"


class Post(BaseModel):
    id: int
    user_id: int
    title: str
    body: str
    birth_date: date
    gender: Gender
    health_status: HealthStatus = HealthStatus.FULLY_HEALTHY
    breed: Optional[str]
    status: Status = Status.FOR_ADOPTION
    images: List[str]
    contact_links: List[str]
    delivery_area: str
    phone: Optional[str]
    created_at: datetime
    updated_at: datetime
    updated_by: Optional[str]
