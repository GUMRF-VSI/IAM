from pydantic import EmailStr, BaseModel, Field

from security.core.base import password_regex


class UserAuth(BaseModel):
    email: EmailStr
    password: str