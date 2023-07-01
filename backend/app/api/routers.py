from fastapi import APIRouter

from api.handlers import auth, user, action, object

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(action.router, prefix="/action", tags=["action"])
api_router.include_router(object.router, prefix="/object", tags=["object"])
