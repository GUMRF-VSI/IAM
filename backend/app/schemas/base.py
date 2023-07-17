from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    last_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]


class ActionBase(BaseModel):
    name: str
    code: str


class ObjectBase(BaseModel):
    name: str
    code: str


class PermissionBase(BaseModel):
    name: str

    object_id: int
    action_id: int


class BaseRole(BaseModel):
    name: str


class ResourceBase(BaseModel):
    name: str
