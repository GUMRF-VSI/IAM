from schemas.base import ObjectBase


class ObjectCreate(ObjectBase):
    ...


class ObjectUpdate(ObjectBase):
    ...


class ObjectORM(ObjectBase):
    id: int

    class Config:
        from_attributes = True
