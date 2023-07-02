from pydantic import BaseModel

from constants.objects import Objects


class ObjectBase(BaseModel):
    name: str
    code: Objects
