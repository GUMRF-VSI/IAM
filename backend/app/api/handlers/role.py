from fastapi import APIRouter, Response, status


from models import role as role_models, permission as permissions_models
from schemas import role as role_schemas
from db.shortcuts import get_object_or_404

router = APIRouter()


@router.post('/create', response_model=role_schemas.RoleORM)
async def create_role(role_data: role_schemas.RoleCreate) -> role_models.Role:
    db_role = role_models.Role(name=role_data.name)
    db_permissions = await permissions_models.Permission.filter(id__in=role_data.permissions)
    await db_role.save()
    await db_role.permissions.add(*db_permissions)
    return db_role


@router.get('/list')
async def roles_list():
    ...


@router.get('/{role_id}', response_model=role_schemas.RoleORM)
async def get_role(role_id: int) -> role_models.Role:
    return await get_object_or_404(role_models.Role, id=role_id)


@router.patch('/{role_id}', response_model=role_schemas.RoleORM)
async def update_role(role_id: int, role_data: role_schemas.RoleUpdate) -> role_models.Role:
    db_role = role_models.Role.update_from_dict(name=role_data.name)
    db_permissions = await permissions_models.Permission.filter(id__in=role_data.permissions)
    await db_role.save()
    await db_role.permissions.add(*db_permissions)


@router.delete('/{role_id}')
async def delete_role(role_id: int) -> Response:
    role = await get_object_or_404(role_models.Role, id=role_id)
    await role.delete()
    return Response(status_code=status.HTTP_200_OK, content='success')
