from pydantic import BaseSettings, BaseModel


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

    SECURITY: SecuritySettings

    @property
    def postgres_db_url(self):
        return f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

    class Config:
        env_file = "../docker/.env"
        case_sensitive = True
        allow_mutation = False
        env_nested_delimiter = '__'


settings = Settings()
