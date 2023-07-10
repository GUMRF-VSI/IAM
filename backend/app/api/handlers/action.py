from typing import List

from fastapi import APIRouter, Response, status, Depends

from models import action as action_models
from schemas import action as action_schemas
from db.shortcuts import get_object_or_404
from config.constants import ActionsTypes
from security.permission import action as action_permissions

router = APIRouter()


@router.post('/create', response_model=action_schemas.ActionORM)
async def create_action(action_data: action_schemas.ActionCreate,
                        user=Depends(action_permissions.can_create)) -> action_models.Action:
    db_action = await action_models.Action.create(**action_data.dict())
    return db_action


@router.get('/list', response_model=List[action_schemas.ActionORM])
async def actions_list(user=Depends(action_permissions.can_retrieve)) -> List[action_models.Action]:
    actions = await action_models.Action.all()
    return actions


@router.get('/{action_id}', response_model=action_schemas.ActionORM)
async def get_action(action_id: int, user=Depends(action_permissions.can_retrieve)) -> action_models.Action:
    db_action = await get_object_or_404(action_models.Action, id=action_id)
    return db_action


@router.patch('/{action_id}', response_model=action_schemas.ActionORM)
async def update_action(action_id: int, action_data: action_schemas.ActionUpdate,
                        user=Depends(action_permissions.can_update)) -> action_models.Action:
    db_action = await get_object_or_404(action_models.Action, id=action_id)
    await db_action.update_from_dict(action_data.dict())
    return db_action


@router.delete('/{action_id}')
async def delete_action(action_id: int, user=Depends(action_permissions.can_delete)):
    db_action = await get_object_or_404(action_models.Action, id=action_id)
    await db_action.delete()
    return Response(status_code=status.HTTP_200_OK, content='success')
