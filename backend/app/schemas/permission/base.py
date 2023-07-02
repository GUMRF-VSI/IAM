from pydantic import BaseModel


class PermissionBase(BaseModel):
    name: str

    object_id: int
    action_id: int
