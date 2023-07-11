from security.permission.base import BasePermission
from models.permission import Permission


class PermissionPermissions(BasePermission):
    ...


permission = PermissionPermissions(Permission)
