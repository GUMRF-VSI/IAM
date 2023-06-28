from datetime import datetime

from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int

    email: str
    last_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]

    is_active: bool = True
    last_login: Optional[datetime]

    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class RoleBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class PermissionBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ObjectBase(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        orm_mode = True


class ActionBase(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        orm_mode = True


class UserSchema(UserBase):
    users: List[UserBase]


class RoleSchema(RoleBase):
    roles: List[RoleBase]


class PermissionSchema(PermissionBase):
    permissions: List[PermissionBase]


class ObjectSchema(ObjectBase):
    objects: List[ObjectBase]


class ActionSchema(ActionBase):
    actions: List[ActionBase]