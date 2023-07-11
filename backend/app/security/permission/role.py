from security.permission.base import BasePermission
from models.role import Role


class RolePermissions(BasePermission):
    ...


role = RolePermissions(Role)
