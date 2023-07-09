from fastapi import HTTPException

from api.exceptions.base import BaseExceptions
from models import Action


class ActionExceptions(BaseExceptions):
    __404_message: str = 'не найдено'


action = ActionExceptions(Action)
