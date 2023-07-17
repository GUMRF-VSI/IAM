from security.permission.base import BasePermission
from models.resource import Resource


class ResourcePermissions(BasePermission):
    ...


resource = ResourcePermissions(Resource)
