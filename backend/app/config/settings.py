from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def postgres_db_url(self):
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

    class Config:
        env_file = "../docker/.env"
        case_sensitive = True
        allow_mutation = False
        env_nested_delimiter = '__'


settings = Settings()
