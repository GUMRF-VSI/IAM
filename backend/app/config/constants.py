from enum import Enum


class ActionsTypes(str, Enum):
    create: str = 'create'
    update: str = 'update'
    retrieve: str = 'retrieve'
    delete: str = 'delete'
