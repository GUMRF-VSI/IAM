from typing import List

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from tortoise.exceptions import OperationalError

from models import role as role_models, permission as permissions_models
from schemas import role as role_schemas
from db.shortcuts import get_object_or_404
from security.permission import role as role_permissions

router = APIRouter()


@router.post('/create', response_model=role_schemas.RoleORM,
             dependencies=[Depends(role_permissions.check_create_permission)])
async def create_role(role_data: role_schemas.RoleCreate) -> role_models.Role:
    db_role = role_models.Role(name=role_data.name)
    db_permissions = await permissions_models.Permission.filter(id__in=role_data.permissions)
    await db_role.save()
    await db_role.permissions.add(*db_permissions)
    return db_role


@router.get('/list', response_model=List[role_schemas.RoleORM],
            dependencies=[Depends(role_permissions.check_retrieve_permission)])
async def roles_list() -> List[role_models.Role]:
    roles = await role_models.Role.all()
    return roles


@router.get('/{role_id}', response_model=role_schemas.RoleORM,
            dependencies=[Depends(role_permissions.check_retrieve_permission)])
async def get_role(role_id: int) -> role_models.Role:
    return await get_object_or_404(role_models.Role, id=role_id)


@router.patch('/{role_id}', response_model=role_schemas.RoleORM,
              dependencies=[Depends(role_permissions.check_update_permission)])
async def update_role(role_id: int, role_data: role_schemas.RoleUpdate) -> role_models.Role:
    db_role = await role_models.Role.update_from_dict(data={'name': role_data.name})
    db_permissions = await permissions_models.Permission.filter(id__in=role_data.permissions)
    await db_role.save()
    await db_role.permissions.add(*db_permissions)
    return db_role


@router.delete('/{role_id}', dependencies=[Depends(role_permissions.check_delete_permission)])
async def delete_role(role_id: int) -> JSONResponse:
    db_role = await get_object_or_404(role_models.Role, id=role_id)
    try:
        await db_role.delete()
    except OperationalError:
        JSONResponse(status_code=status.HTTP_200_OK, content={'success': False})
    return JSONResponse(status_code=status.HTTP_200_OK, content={'success': True})
