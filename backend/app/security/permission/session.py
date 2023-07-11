from security.permission.base import BasePermission
from models.session import Session


class SessionPermissions(BasePermission):
    ...


session = SessionPermissions(Session)
