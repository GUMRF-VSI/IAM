from typing import Optional, List, Dict

from pydantic import BaseModel, EmailStr


class _Permission(BaseModel):
    obj: str
    action: List[str]


class _Role(BaseModel):
    permission: List[_Permission]


class AccessTokenData(BaseModel):
    iat: int
    exp: int
    auth_time: int
    sub: str
    sid: str
    typ: str = 'Bearer'
    roles: List[Dict]


class RefreshTokenData(BaseModel):
    iat: int
    exp: int

    sub: str
    sid: str
    typ: str = 'Refresh'


class IdentityTokenData(BaseModel):
    iat: int
    exp: int

    typ: str = 'Identity'

    sub: str
    sid: str

    email: EmailStr

    last_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]

    is_active: bool


class Tokens(BaseModel):
    access: str
    refresh: str
    identity: str


class AccessToken(BaseModel):
    access: str


class RefreshToken(BaseModel):
    refresh: str
