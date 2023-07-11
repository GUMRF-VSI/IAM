from security.permission.base import BasePermission
from models.user import User


class UserPermissions(BasePermission):
    ...


user = UserPermissions(User)
