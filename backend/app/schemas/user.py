from typing import List

from datetime import datetime

from typing import Optional

from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from pydantic import Field, BaseModel

from schemas.base import UserBase
from security.core.base import password_regex
from models import User


class ResetPassword(BaseModel):
    old_password: str
    new_password: str


class UserORM(UserBase):
    id: int

    is_staff: bool
    is_active: bool

    last_login: Optional[datetime]

    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class UserORMList(BaseModel):
    users: List[UserORM]


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    ...


class UserFilters(BaseModel):
    is_staff: bool
