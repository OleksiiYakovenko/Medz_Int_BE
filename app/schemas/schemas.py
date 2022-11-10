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


class Users(BaseModel):
    user_id: int
    email: str
    password: str
    user_name: str
    user_bio: str
    creation_date: str


class UsersIn(BaseModel):
    user_id: int
    email: str
    password: str
    user_name: str
    user_bio: str
    creation_date: str


class SignIn(BaseModel):
    pass


class RequestModel(BaseModel):
    pass


class SignUp(BaseModel):
    pass


class RequestModel(BaseModel):
    pass


class UserUpdate(BaseModel):
    pass


class Request(BaseModel):
    pass


class Model(BaseModel):
    pass


class ListResponse(BaseModel):
    pass

