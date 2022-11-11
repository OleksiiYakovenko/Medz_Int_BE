import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from app.schemas.schemas import settings


DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}"

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
Base = declarative_base()

metadata = sqlalchemy.MetaData()
metadata.create_all(engine)



