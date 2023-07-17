import logging

from fastapi import FastAPI

from api.routers import api_router
from core.settings import settings
from db.database import init_db, init_models
from models.utils.user import create_first_superuser

logger = logging.getLogger("uvicorn")

app = FastAPI(title=settings.PROJECT_NAME, )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup_event():
    logger.info("Start actions on startup application...")
    init_models()
    init_db(app)
    logger.info("Finish actions on startup application...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
