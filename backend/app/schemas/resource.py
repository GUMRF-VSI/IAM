from schemas.base import ResourceBase


class ResourceCreate(ResourceBase):
    ...


class ResourceUpdate(ResourceBase):
    ...


class ResourceORM(ResourceBase):
    id: int
    token: str

    class Config:
        from_attributes = True
