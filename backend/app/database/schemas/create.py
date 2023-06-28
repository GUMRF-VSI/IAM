from database.schemas import base


class UserCreateSchema(base.UserBase):
    password: str


class RoleCreateSchema(base.RoleBase):
    ...


class PermissionCreateSchema(base.PermissionBase):
    ...


class ObjectCreateSchema(base.ObjectBase):
    ...


class ActionsCreateSchema(base.ActionBase):
    ...
