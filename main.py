from fastapi import FastAPI
import uvicorn
from app.schemas.schemas import settings
from starlette.middleware.cors import CORSMiddleware
from app.routes.route import router
from app.database.db import database


app = FastAPI()


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)

