import uvicorn
from app.config import settings


if __name__ == "__main__":
    uvicorn.run("app.app:app", host=settings.SERVER_HOST, port=settings.PORT_SERVER)