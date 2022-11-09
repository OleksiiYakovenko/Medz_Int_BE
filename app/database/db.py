import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


DATABASE_URL = "postgresql://postgres:Rfvxfnrf1@localhost/medintDB"

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
Base = declarative_base()

metadata = sqlalchemy.MetaData()
metadata.create_all(engine)



