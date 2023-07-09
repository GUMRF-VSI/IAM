from fastapi import HTTPException

from api.exceptions.base import BaseExceptions
from models import Object


class ObjectExceptions(BaseExceptions):
    ...


obj = ObjectExceptions(Object)
