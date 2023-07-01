from typing import Optional

from pydantic import BaseModel, EmailStr

from config.settings import settings


class AccessTokenData(BaseModel):
    exp: int
    sub: str


class RefreshData(BaseModel):
    id: str
    email: str


class IdentityData(BaseModel):
    email: EmailStr
    last_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]


class TokenData(BaseModel):
    access: str
    refresh: str
    identity: str

