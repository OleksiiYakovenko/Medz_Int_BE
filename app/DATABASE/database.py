from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{0}:{1}@{2}:{3}/{4}".format(
    settings.POSTGRES_USER,
    settings.POSTGRES_PASSWORD,
    settings.POSTGRES_HOSTNAME,
    settings.POSTGRES_PORT,
    settings.POSTGRES_DB

)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


async def create_postgres_connection():
    create_engine(f"postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
        settings.POSTGRES_USER,
        settings.POSTGRES_PASSWORD,
        settings.POSTGRES_HOSTNAME,
        settings.POSTGRES_PORT,
        settings.POSTGRES_DB)
    )
    print("DB connection closed")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()