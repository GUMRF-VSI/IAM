from security.permission.base import BasePermission
from models.action import Action


class ActionPermissions(BasePermission):
    ...


action = ActionPermissions(Action)
