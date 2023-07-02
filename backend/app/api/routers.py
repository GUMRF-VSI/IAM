from fastapi import APIRouter

from api.handlers import auth, user, action, object, permission, role

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(action.router, prefix="/action", tags=["action"])
api_router.include_router(permission.router, prefix="/permissions", tags=["permissions"])
api_router.include_router(role.router, prefix="/role", tags=["role"])
