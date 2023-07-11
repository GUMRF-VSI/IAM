from pydantic import BaseModel
from pydantic_settings import BaseSettings


class SecuritySettings(BaseModel):
    ALGORITHM: str = "HS256"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 15
    IDENTITY_TOKEN_EXPIRE_MINUTES: int = 15


class Settings(BaseSettings):
    PROJECT_NAME: str = 'AuthService'

    API_V1_STR: str = '/api/v1'

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    DEBUG:bool = False

    SECURITY: SecuritySettings

    APP_MODELS: list = ["models.user", "models.action", "models.object", "models.permission", "models.role",
                        "models.session"]

    @property
    def postgres_db_url(self):
        return f'postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

    @property
    def models(self):
        return self.APP_MODELS + ['aerich.models']

    class Config:
        case_sensitive = True
        env_nested_delimiter = '__'


settings = Settings()
