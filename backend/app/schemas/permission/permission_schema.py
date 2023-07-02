from typing import List

from pydantic import BaseModel

from schemas.permission.base import PermissionBase


class CreatePermission(PermissionBase):
    ...


class PermissionUpdate(PermissionBase):
    ...


class PermissionList(BaseModel):
    class Permission(PermissionBase):
        id: int

    permissions: List[Permission]


class PermissionORM(PermissionBase):
    id: int

    class Config:
        orm_mode = True
