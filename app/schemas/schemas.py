from pydantic import BaseModel, BaseSettings
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

    SERVER_HOST: str
    SERVER_PORT: int


    class Env:
        env_file = '.env'
        env_file_encoding = 'utf-8'



settings = Settings()


class User(BaseModel):
    email: str

    class Config:
        orm_mode = True


class CreateUser(User):
    password: str


class ActiveUser(User):
    user_id: int
