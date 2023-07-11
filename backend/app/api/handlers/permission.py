from typing import List

from fastapi import APIRouter, Response, status, Depends

from schemas import permission as permission_schemas
from models import permission as permission_models
from db.shortcuts import get_object_or_404
from security.permission import permission

router = APIRouter()


@router.post('/create', response_model=permission_schemas.PermissionORM,
             dependencies=[Depends(permission.check_create_permission)])
async def create_permission(permission_data: permission_schemas.PermissionCreate) -> permission_models.Permission:
    db_permission = await permission_models.Permission.create(**permission_data.dict())
    return db_permission


@router.get('/list', response_model=List[permission_schemas.PermissionORM],
            dependencies=[Depends(permission.check_retrieve_permission)])
async def permissions_list() -> List[permission_models.Permission]:
    permissions = await permission_models.Permission.all()
    return permissions


@router.get('/{permission_id}', response_model=permission_schemas.PermissionORM,
            dependencies=[Depends(permission.check_retrieve_permission)])
async def get_permission(permission_id: int) -> permission_models.Permission:
    db_permission = await get_object_or_404(permission_models.Permission, id=permission_id)
    return db_permission


@router.patch('/{permission_id}', response_model=permission_schemas.PermissionORM,
              dependencies=[Depends(permission.check_update_permission)])
async def update_permission(permission_id: int,
                            permission_data: permission_schemas.PermissionUpdate) -> permission_models.Permission:
    db_permission = await get_object_or_404(permission_models.Permission, id=permission_id)
    await db_permission.update_from_dict(permission_data.dict())
    return db_permission


@router.delete('/{permission_id}', dependencies=[Depends(permission.check_delete_permission)])
async def delete_permission(permission_id: int) -> Response:
    db_permission = await get_object_or_404(permission_models.Permission, id=permission_id)
    await db_permission.delete()
    return Response(status_code=status.HTTP_200_OK, content='success')
