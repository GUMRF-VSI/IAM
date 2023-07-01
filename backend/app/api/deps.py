from typing import Generator

from database.core.session import SessionLocal


def get_database() -> Generator:
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
