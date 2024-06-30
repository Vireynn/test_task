import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from models import db_helper, Base
from ads import advert_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield

app = FastAPI()
app.include_router(router=advert_router, prefix="/adverts")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
