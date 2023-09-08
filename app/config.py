from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str = 'postgres'
    DB_PASSWORD: str = 'localhost'
    DB_HOSTNAME: str
    DB_PORT: int
    DB_NAME: str
    SECRET_KEY: str = 'fjklasjdflk34'
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE: int

    class Config:
        env_file = '.env',


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
