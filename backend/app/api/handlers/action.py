from typing import List

from fastapi import APIRouter, Response, status, Depends

from models import action as action_models
from schemas import action as action_schemas
from db.shortcuts import get_object_or_404
from security.permission import action

router = APIRouter()


@router.post('/create', response_model=action_schemas.ActionORM, dependencies=[Depends(action.check_create_permission)])
async def create_action(action_data: action_schemas.ActionCreate) -> action_models.Action:
    db_action = await action_models.Action.create(**action_data.dict())
    return db_action


@router.get('/list', response_model=List[action_schemas.ActionORM],
            dependencies=[Depends(action.check_retrieve_permission)])
async def actions_list() -> List[action_models.Action]:
    actions = await action_models.Action.all()
    return actions


@router.get('/{action_id}', response_model=action_schemas.ActionORM,
            dependencies=[Depends(action.check_retrieve_permission)])
async def get_action(action_id: int) -> action_models.Action:
    db_action = await get_object_or_404(action_models.Action, id=action_id)
    return db_action


@router.patch('/{action_id}', response_model=action_schemas.ActionORM,
              dependencies=[Depends(action.check_update_permission)])
async def update_action(action_id: int, action_data: action_schemas.ActionUpdate) -> action_models.Action:
    db_action = await get_object_or_404(action_models.Action, id=action_id)
    await db_action.update_from_dict(action_data.dict())
    return db_action


@router.delete('/{action_id}', dependencies=[Depends(action.check_delete_permission)])
async def delete_action(action_id: int):
    db_action = await get_object_or_404(action_models.Action, id=action_id)
    await db_action.delete()
    return Response(status_code=status.HTTP_200_OK, content='success')
