from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_HOSTNAME: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

    SERVER_HOST: str
    PORT_SERVER: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()