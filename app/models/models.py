from sqlalchemy import Column, String, Integer, ForeignKey
from app.database.db import Base
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

