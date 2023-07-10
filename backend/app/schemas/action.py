from schemas.base import ActionBase


class ActionCreate(ActionBase):
    ...


class ActionUpdate(ActionBase):
    ...


class ActionORM(ActionBase):
    id: int

    class Config:
        from_attributes = True
