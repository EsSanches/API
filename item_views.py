from typing import Annotated
from fastapi import APIRouter, Path

# прослойка маршрутов не подключая к основному приложению
router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def list_item():
    return ["item_1", "item_2", "item_3",]

# самый последний добавленный товар
@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": 0, "name": "latest"}}

# получить item по id
@router.get("/{item_id}/")
def get_item_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {"item": {"id": item_id}}