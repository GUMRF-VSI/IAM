from typing import Optional

from pydantic import BaseModel, Field, EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class SecuritySettings(BaseModel):
    ALGORITHM: str = "HS256"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE: int = Field(default=60, description='Access token expired time in seconds')
    REFRESH_TOKEN_EXPIRE: int = Field(default=900, description='Access token expired time in seconds')
    IDENTITY_TOKEN_EXPIRE: int = Field(default=900, description='Access token expired time in seconds')


class SuperUser(BaseModel):
    EMAIL: EmailStr = Field(alias='email')
    LAST_NAME: Optional[str] = Field(alias='last_name')
    FIRST_NAME: Optional[str] = Field(alias='first_name')
    MIDDLE_NAME: Optional[str] = Field(alias='middle_name')
    PASSWORD: str = Field(alias='password')


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', env_nested_delimiter='__')
    PROJECT_NAME: str = 'AuthService'

    API_V1_STR: str = '/api/v1'

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    SUPERUSER: SuperUser

    DEBUG: bool = False

    SECURITY: SecuritySettings

    APP_MODELS: list = ["models.user", "models.action", "models.object", "models.permission", "models.role",
                        "models.session"]

    @property
    def postgres_db_url(self):
        return f'postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

    @property
    def models(self):
        return self.APP_MODELS + ['aerich.models']

    # class Config:
    #     case_sensitive = True
    #     env_nested_delimiter = '__'


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
