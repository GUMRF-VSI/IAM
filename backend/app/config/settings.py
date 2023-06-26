from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str

    class Config:
        case_sensitive = True
        allow_mutation = False
        env_nested_delimiter = '__'


settings = Settings()
