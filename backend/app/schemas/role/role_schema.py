from pydantic import BaseModel

from schemas.role.base import RoleBase


class CreateRole(RoleBase):
    ...


class RoleORM(RoleBase):
    id: int
