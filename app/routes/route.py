from fastapi import APIRouter, Depends, HTTPException
from app.CRUD import crud
from app.schemas import schemas
from app.models import models
from sqlalchemy.orm import Session
from app.database.db import SessionLocal


router = APIRouter(prefix='', tags=[''])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/health-check')
def health_check():
    return {'Status': 'Working'}



@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    new_user = crud.get_user_by_email(db, email=user.email)
    if new_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/users/{user_id}")
def delete_user(user_id, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.user_id == user_id)
    user.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


@router.put("/users/{user_id}")
def update_user(user_id, request: schemas.User, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.user_id == user_id)
    if not user.first():
        raise HTTPException(status_code=404)
    user.update(request.dict(), synchronize_session=False)
    db.commit()
    return 'updated'
