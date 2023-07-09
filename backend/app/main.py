from fastapi import FastAPI

from api.routers import api_router
from config.settings import settings
from db.database import init_db

app = FastAPI(title=settings.PROJECT_NAME, )

init_db(app=app)

app.include_router(api_router, prefix=settings.API_V1_STR)
