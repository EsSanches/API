from contextlib import asynccontextmanager

from fastapi import FastAPI, Path
import uvicorn

# from pydantic import EmailStr, BaseModel
from core.models import Base, db_helper
from item_views import router as items_router
from users.views import router as users_router


# события цикла жизни lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# приветствие
@app.get("/hello/")
def hello(name: str = "Незнакомец"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


# новый маршрут
@app.get("/custom/")
def read_custom_message():
    return {"message": "this is a custom message!"}


@app.post("/calc/add/")
def calc(a: int, b: int):
    return {"a": a, "b": b, "res": a + b}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
