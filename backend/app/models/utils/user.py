from typing import List, Dict

from models import User, Permission


async def get_permissions(permissions: Permission) -> List[Dict]:
    permissions_list = list()

    for permission in permissions:
        print(permission.name)
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

    print(user_roles)

    return user_roles
