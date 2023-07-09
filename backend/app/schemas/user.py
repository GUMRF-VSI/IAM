from typing import List

from datetime import datetime

from typing import Optional

from pydantic import Field

from schemas.base import UserBase
from security.core.base import password_regex


class UserCreate(UserBase):
    password: str
