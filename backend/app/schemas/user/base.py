from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    last_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]