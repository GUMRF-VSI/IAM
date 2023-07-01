from fastapi import FastAPI

from api.routers import api_router
from config.settings import settings

app = FastAPI(title=settings.PROJECT_NAME, )

app.include_router(api_router, prefix=settings.API_V1_STR)
