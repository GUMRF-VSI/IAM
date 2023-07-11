from typing import TypeVar, Type

from functools import wraps

from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from models.base.base_model import CustomModel
from config.constants import ActionsTypes
from models import user as user_models
from api import exceptions
from security.utils.token import validate_access_token

ModelType = TypeVar("ModelType", bound=CustomModel)

token_key = HTTPBearer()


class BasePermission:
    model: ModelType
    actions: ActionsTypes = ActionsTypes

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def __check_permissions(self, token: str, action: ActionsTypes) -> bool:
        token_data = await validate_access_token(token)
        user = await user_models.User.filter(uuid=token_data.sub)
        if not user:
            raise exceptions.token.invalid_token
        for role in token_data.roles:
            for obj, actions in role.items():
                if obj == self.model.table and action.name in actions:
                    return True
        raise exceptions.user.forbidden

    async def check_create_permission(self, auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> bool:
        return await self.__check_permissions(auth_token.credentials, self.actions.create)

    async def check_delete_permission(self, auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> bool:
        return await self.__check_permissions(auth_token.credentials, self.actions.delete)

    async def check_retrieve_permission(self, auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> bool:
        return await self.__check_permissions(auth_token.credentials, self.actions.retrieve)

    async def check_update_permission(self, auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> bool:
        return await self.__check_permissions(auth_token.credentials, self.actions.update)
