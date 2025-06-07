from fastapi import FastAPI
import uvicorn
from pydantic import EmailStr, BaseModel

app = FastAPI()

class Users(BaseModel):
    email: EmailStr

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

# ипользовать метод post
@app.post("/users/")
def create_user(user: Users):
    return {"message": "success", "email": user.email}

@app.post("/calc/add/")
def calc(a: int, b: int):
    return {"a": a, "b": b, "res": a + b}

@app.get("/items/")
def list_item():
    return ["item_1", "item_2", "item_3",]

# самый последний добавленный товар
@app.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": 0, "name": "latest"}}

# получить item по id
@app.get("/items/{item_id}/")
def get_item_id(item_id: int):
    return {"item": {"id": item_id}}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)