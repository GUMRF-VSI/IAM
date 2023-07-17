from typing import List

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from tortoise import exceptions

from db.shortcuts import get_object_or_404
from models import resource as resource_models
from schemas import resource as resource_schemas
from security.permission.resource import resource as resource_permissions

router = APIRouter()


@router.post('/create', response_model=resource_schemas.ResourceORM,
             dependencies=[Depends(resource_permissions.check_create_permission)])
async def create_resource(resource_data: resource_schemas.ResourceCreate) -> resource_models.Resource:
    return await resource_models.Resource.create(**resource_data.model_dump())


@router.get('/', response_model=List[resource_schemas.ResourceORM],
            dependencies=[Depends(resource_permissions.check_retrieve_permission)])
async def get_resources() -> List[resource_models.Resource]:
    resources = await resource_models.Resource.all()
    return resources


@router.get('/{resource_id}', response_model=resource_schemas.ResourceORM,
            dependencies=[Depends(resource_permissions.check_retrieve_permission)])
async def retrieve_resource(resource_id) -> resource_models.Resource:
    return await get_object_or_404(resource_models.Resource, id=resource_id)


@router.patch('/{resource_id}', response_model=resource_schemas.ResourceORM,
              dependencies=[Depends(resource_permissions.check_update_permission)])
async def update_resource(resource_id: int, resource_data: resource_schemas.ResourceUpdate):
    resource = await get_object_or_404(resource_models.Resource, id=resource_id)
    await resource.update_from_dict(resource_data.model_dump())
    return resource


@router.delete('/{resource_id}', response_model=resource_schemas.ResourceORM,
               dependencies=[Depends(resource_permissions.check_delete_permission)])
async def delete_resource_token(resource_id: int) -> JSONResponse:
    resource = await get_object_or_404(resource_models.Resource, id=resource_id)
    try:
        await resource.delete()
    except exceptions.OperationalError:
        JSONResponse(status_code=status.HTTP_200_OK, content={'success': False})
    return JSONResponse(status_code=status.HTTP_200_OK, content={'success': True})
