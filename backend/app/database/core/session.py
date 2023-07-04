from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings


postgres_engin = create_engine(settings.postgres_db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engin)
