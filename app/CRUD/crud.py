from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.CreateUser):
    fake_hashed_password = user.password + "notreallyhashed"
    new_user = models.Users(email=user.email, hashed_password=fake_hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
