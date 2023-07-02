from pydantic import BaseModel

from constants.actions import Actions


class ActionBase(BaseModel):
    name: str
    code: Actions
