from fastapi import APIRouter

from api.handlers import auth, user, action, object, permission, role, resource, internal

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(action.router, prefix="/action", tags=["action"])
api_router.include_router(object.router, prefix="/object", tags=["object"])
api_router.include_router(permission.router, prefix="/permission", tags=["permission"])
api_router.include_router(role.router, prefix="/role", tags=["role"])
api_router.include_router(resource.router, prefix="/resource", tags=["resource"])

# Internal routers
api_router.include_router(internal.router, prefix="/internal", tags=["internal"])
