import logging

from fastapi import FastAPI

from api.routers import api_router
from config.settings import settings
from db.database import init_db

logger = logging.getLogger("uvicorn")

app = FastAPI(title=settings.PROJECT_NAME, )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup_event():
    logger.info("Init database")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
