from pydantic import BaseModel


class Users(BaseModel):
    user_id: int
    email: str
    password: str


class UsersIn(BaseModel):
    user_id: int
    email: str
    password: str


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

