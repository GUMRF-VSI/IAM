from typing import List

from fastapi import APIRouter, Response, status, Depends

from models import object as object_models
from schemas import object as object_schemas
from db.shortcuts import get_object_or_404
from security import permission

router = APIRouter()


@router.post('/create', response_model=object_schemas.ObjectORM)
async def create_object(object_data: object_schemas.ObjectCreate,
                        user: object_models.Object = Depends(permission.obj.can_create)) -> object_models.Object:
    db_object = await object_models.Object.create(**object_data.dict())
    return db_object


@router.get('/list', response_model=List[object_schemas.ObjectORM])
async def objects_list(user: object_models.Object = Depends(permission.obj.can_create)) -> List[object_models.Object]:
    objects = await object_models.Object.all()
    return objects


@router.get('/{object_id}', response_model=object_schemas.ObjectORM)
async def get_object(object_id: int,
                     user: object_models.Object = Depends(permission.obj.can_create)) -> object_models.Object:
    db_object = await get_object_or_404(object_models.Object, id=object_id)
    return db_object


@router.patch('/{object_id}', response_model=object_schemas.ObjectORM)
async def update_object(object_id: int, object_data: object_schemas.ObjectUpdate,
                        user: object_models.Object = Depends(permission.obj.can_create)) -> object_models.Object:
    db_object = await get_object_or_404(object_models.Object, id=object_id)
    await db_object.update_from_dict(object_data.dict())
    return db_object


@router.delete('/{object_id}')
async def delete_object(object_id: int,
                        user: object_models.Object = Depends(permission.obj.can_create)) -> Response:
    db_object = await get_object_or_404(object_models.Object, id=object_id)
    await db_object.delete()
    return Response(status_code=status.HTTP_200_OK, content='success')
