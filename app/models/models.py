from sqlalchemy import Column, String, Integer, DateTime
from app.database.db import Base


class Users(Base):
    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String(350), unique=True)
    password = Column(String(350), unique=True)
    user_name = Column(String(350))
    user_bio = Column(String(350))
    creation_date = Column(DateTime)


Users = Users.__table__
