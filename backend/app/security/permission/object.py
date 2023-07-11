from security.permission.base import BasePermission
from models.object import Object


class ObjectPermissions(BasePermission):
    ...


obj = ObjectPermissions(Object)
