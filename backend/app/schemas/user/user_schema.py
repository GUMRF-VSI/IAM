from typing import List

from datetime import datetime

from typing import Optional

from schemas.user.base import UserBase
from schemas.role import RoleORM


class UserCreate(UserBase):
    password: str


class UsersList(UserBase):
    class User(UserBase):
        id: int

    users: List[User]


class UserORM(UserBase):
    id: str

    is_active: bool = True
    last_login: Optional[datetime]

    created_at: datetime
    updated_at: Optional[datetime]

    roles: List[RoleORM]

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    ...
