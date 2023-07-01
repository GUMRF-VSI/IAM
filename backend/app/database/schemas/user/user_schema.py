from typing import List

from datetime import datetime

from typing import Optional

from database.schemas.user import base


class UserCreate(base.UserBase):
    password: str


class UsersListSchema(base.UserBase):
    users: List[base.UserBase]


class User(base.UserBase):
    id: int

    is_active: bool = True
    last_login: Optional[datetime]

    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class UserUpdate(base.UserBase):
    ...
