from typing import List

from pydantic import BaseModel

from schemas.action.base import ActionBase


class CreateAction(ActionBase):
    ...


class ActionsList(BaseModel):
    class Action(ActionBase):
        id: int

    actions: List[Action]


class ActionUpdate(ActionBase):
    ...


class ActionORM(ActionBase):
    id: int

    class Config:
        orm_mode = True
