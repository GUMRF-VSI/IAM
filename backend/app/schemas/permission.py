from schemas.base import PermissionBase


class PermissionCreate(PermissionBase):
    ...


class PermissionUpdate(PermissionBase):
    ...


class PermissionORM(PermissionBase):
    id: int

    class Config:
        from_attributes = True
