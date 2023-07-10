from typing import List

from schemas.base import BaseRole
from models.permission import Permission


class RoleCreate(BaseRole):
    permissions: List[int]


class RoleUpdate(BaseRole):
    ...


class RoleORM(BaseRole):
    id: int

    class Config:
        from_attributes = True
