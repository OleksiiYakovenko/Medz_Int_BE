from fastapi import APIRouter
from typing import List
from app.models.models import Users
from app.schemas.schemas import Users, UsersIn
from app.database.db import database


router = APIRouter(prefix='', tags=['Health'])


@router.get('/health-check')
def health_check():
    return {'Status': 'Working'}


@router.get("/Users/", response_model=List[Users])
async def read_user_table():
    query = Users.select()
    return await database.fetch_all(query)


@router.post("/Users/", response_model=Users)
async def create_user_in_table(Users: UsersIn):
    query = Users.insert().values(text=Users.text, completed=Users.completed)
    last_record_id = await database.execute(query)
    return {**Users.dict(), "id": last_record_id}

