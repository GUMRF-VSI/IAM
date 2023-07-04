from typing import Optional, List

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

    sub: int
    typ: str = 'Bearer'
    # roles: List[_Role]


class RefreshData(BaseModel):
    iat: int
    exp: int
    sub: int
    tup: str = 'Refresh'
    sid: str


class IdentityData(BaseModel):
    iat: int
    exp: int

    typ: str = 'Identity'

    email: EmailStr

    last_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]

    is_active: bool


class TokenData(BaseModel):
    access: str
    refresh: str
    identity: str
