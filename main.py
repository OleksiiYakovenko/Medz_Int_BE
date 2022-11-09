from fastapi import FastAPI
from typing import List
from app.models.models import Users
from app.schemas.schemas import Users, UsersIn
from app.database.db import database


app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "Working"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/Users/", response_model=List[Users])
async def read_notes():
    query = Users.select()
    return await database.fetch_all(query)


@app.post("/Users/", response_model=Users)
async def create_note(Users: UsersIn):
    query = Users.insert().values(text=Users.text, completed=Users.completed)
    last_record_id = await database.execute(query)
    return {**Users.dict(), "id": last_record_id}

