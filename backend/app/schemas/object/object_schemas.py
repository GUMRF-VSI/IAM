from typing import List

from pydantic import BaseModel

from schemas.object.base import ObjectBase


class CreateObject(ObjectBase):
    ...


class ObjectUpdate(ObjectBase):
    ...


class ObjectsList(BaseModel):
    class Object(ObjectBase):
        id: int

    objects: List[Object]


class ObjectORM(ObjectBase):
    id: int

    class Config:
        orm_mode = True
