from sqlalchemy import Column, String, Integer
from app.database.db import Base


class Users(Base):
    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String(350))
    password = Column(String(350), unique=True)


Users = Users.__table__
