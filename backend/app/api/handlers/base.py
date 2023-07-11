# from typing import List, TypeVar, Type
#
# from fastapi import APIRouter, Response, status
#
# from models import object as object_models
# from schemas import object as object_schemas
# from db.shortcuts import get_object_or_404
# from security.permission import obj
# from models.base.base_model import CustomModel
# from security.permission.base import BasePermission
#
#
# ModelType = TypeVar("ModelType", bound=CustomModel)
# PermissionType = TypeVar('PermissionType', bound=BasePermission)
#
# class BaseHandler:
#     router = APIRouter()
#     permissions_class: Type[PermissionType]
#     def __init__(self, permissions_class: Type[PermissionType], nodel: Type[ModelType]):
#         self.permissions_class = permissions_class
#         self.router = APIRouter()
#         self.__init_routers()
#
#     def __init_routers(self):
#         self.router.add_api_route("/create", self.hello, methods=["POST"], response_model=)
#         self.router.add_api_route("/list", self.hello, methods=["GET"])
#         self.router.add_api_route("/{obj_id}", self.hello, methods=["GET"])
#         self.router.add_api_route("/{obj_id}", self.hello, methods=["PATCH"])
#         self.router.add_api_route("/{obj_id}", self.hello, methods=["DELETE"])
#
#     @router.post('/create', response_model=action_schemas.ActionORM)
#     @action.create_permission
#     async def create_action(action_data: action_schemas.ActionCreate) -> action_models.Action:
#         db_action = await action_models.Action.create(**action_data.dict())
#         return db_action
#
#     @router.get('/list', response_model=List[action_schemas.ActionORM])
#     @action.retrieve_permission
#     async def actions_list() -> List[action_models.Action]:
#         actions = await action_models.Action.all()
#         return actions
#
#     @router.get('/{action_id}', response_model=action_schemas.ActionORM)
#     @action.retrieve_permission
#     async def get_action(action_id: int) -> action_models.Action:
#         db_action = await get_object_or_404(action_models.Action, id=action_id)
#         return db_action
#
#     @router.patch('/{action_id}', response_model=action_schemas.ActionORM)
#     @action.update_permission
#     async def update_action(action_id: int, action_data: action_schemas.ActionUpdate) -> action_models.Action:
#         db_action = await get_object_or_404(action_models.Action, id=action_id)
#         await db_action.update_from_dict(action_data.dict())
#         return db_action
#
#     @router.delete('/{action_id}')
#     @action.delete_permission
#     async def delete_action(action_id: int):
#         db_action = await get_object_or_404(action_models.Action, id=action_id)
#         await db_action.delete()
#         return Response(status_code=status.HTTP_200_OK, content='success')
#
#     def hello(self):
#         return {"Hello": self.name}