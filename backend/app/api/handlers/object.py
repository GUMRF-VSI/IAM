from typing import List

from fastapi import APIRouter, Response, status, Depends

from models import object as object_models
from schemas import object as object_schemas
from db.shortcuts import get_object_or_404
from security.permission import obj

router = APIRouter()


@router.post('/create', response_model=object_schemas.ObjectORM,
             dependencies=[Depends(obj.check_create_permission)])
async def create_object(object_data: object_schemas.ObjectCreate) -> object_models.Object:
    db_object = await object_models.Object.create(**object_data.dict())
    return db_object


@router.get('/list', response_model=List[object_schemas.ObjectORM],
            dependencies=[Depends(obj.check_retrieve_permission)])
async def objects_list() -> List[object_models.Object]:
    objects = await object_models.Object.all()
    return objects


@router.get('/{object_id}', response_model=object_schemas.ObjectORM,
            dependencies=[Depends(obj.check_retrieve_permission)])
async def get_object(object_id: int) -> object_models.Object:
    db_object = await get_object_or_404(object_models.Object, id=object_id)
    return db_object


@router.patch('/{object_id}', response_model=object_schemas.ObjectORM,
              dependencies=[Depends(obj.check_update_permission)])
async def update_object(object_id: int, object_data: object_schemas.ObjectUpdate) -> object_models.Object:
    db_object = await get_object_or_404(object_models.Object, id=object_id)
    await db_object.update_from_dict(object_data.dict())
    return db_object


@router.delete('/{object_id}', dependencies=[Depends(obj.check_delete_permission)])
async def delete_object(object_id: int) -> Response:
    db_object = await get_object_or_404(object_models.Object, id=object_id)
    await db_object.delete()
    return Response(status_code=status.HTTP_200_OK, content='success')
