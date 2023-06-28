from typing import List

from database.schemas import base


class UsersSchema(base.UserBase):
    users: List[base.UserBase]


class RolesSchema(base.RoleBase):
    roles: List[base.RoleBase]


class PermissionsSchema(base.PermissionBase):
    permissions: List[base.PermissionBase]


class ObjectsSchema(base.ObjectBase):
    objects: List[base.ObjectBase]


class ActionsSchema(base.ActionBase):
    actions: List[base.ActionBase]
