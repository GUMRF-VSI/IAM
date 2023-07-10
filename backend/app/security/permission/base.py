from typing import TypeVar, Type

from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from models.base.base_model import CustomModel
from config.constants import ActionsTypes
from models import user as user_models
from api.exceptions import user as user_exceptions
from security.utils.token import validate_access_token

ModelType = TypeVar("ModelType", bound=CustomModel)

token_key = HTTPBearer()


class BasePermission:
    model: ModelType
    actions: ActionsTypes = ActionsTypes

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def __check_permissions(self, token: str, action: ActionsTypes) -> Type[ModelType]:
        token_data = await validate_access_token(token)
        for role in token_data.roles:
            for obj, actions in role.items():
                if obj == self.model.table and action.name in actions:
                    return await self.model.filter(uuid=token_data.sub).first()
        raise user_exceptions.forbidden

    async def can_create(self, auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> Type[ModelType]:
        return await self.__check_permissions(auth_token.credentials, self.actions.create)

    async def can_delete(self, auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> Type[ModelType]:
        return await self.__check_permissions(auth_token.credentials, self.actions.delete)

    async def can_retrieve(self, auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> Type[ModelType]:
        return await self.__check_permissions(auth_token.credentials, self.actions.retrieve)

    async def can_update(self, auth_token: HTTPAuthorizationCredentials = Security(token_key)) -> Type[ModelType]:
        return await self.__check_permissions(auth_token.credentials, self.actions.update)
