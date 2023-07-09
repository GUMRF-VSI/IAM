from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from config.settings import settings

# MODELS = {'models': [settings.MODELS] + ['aerich.models']}


TORTOISE_ORM = {
    "connections": {"default": settings.postgres_db_url},
    "apps": {
        "models": {
            "models": settings.models,
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=settings.postgres_db_url,
        modules={'models': settings.models},
        generate_schemas=False,
        add_exception_handlers=True,
    )
