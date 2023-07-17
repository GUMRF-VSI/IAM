import logging

from typing import List, Dict

from models import User, Permission
from core.settings import settings


logger = logging.getLogger("uvicorn")


def create_first_superuser():
    logger.info('Creating first superuser')
    is_user_exist = User.filter(email=settings.SUPERUSER.EMAIL).exists()
    print(is_user_exist)
    if not is_user_exist:
        user_data = settings.SUPERUSER.model_dump(by_alias=True)
        user_data.update(is_superuser=True)
        User.create(user_data)
        logger.info('Superuser successfully created')
    logger.info('Superuser already exist')


async def get_permissions(permissions: Permission) -> List[Dict]:
    permissions_list = list()
    for permission in permissions:
        new_item = True
        action = await permission.action.all()
        obj = await permission.object.all()

        for item in permissions_list:
            item_index = permissions_list.index(item)
            if obj.code in item.keys() and new_item:
                permissions_list[item_index][obj.code].append(action.code)
                new_item = False

        if new_item:
            permissions_list.append({obj.code: [action.code]})

    return permissions_list


async def get_user_riles(user: User) -> List[Dict]:
    user_roles = list()

    roles = await user.roles.all()
    for role in roles:
        permissions = await role.permissions.all()
        permission_data = await get_permissions(permissions)
        role_data = {role.name: permission_data}
        user_roles.append(role_data)
    return user_roles
