from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends, Body

from app.core.database import get_item_repository
from app.core.models import Item
from app.core.repositories import ItemRepository

router = APIRouter()


@router.post("/items/")
async def create_item(item: Item = Body(...), repository: ItemRepository = Depends(get_item_repository)):
    item_id = repository.create(item)
    return {"id": str(item_id)}


@router.get("/items/{item_id}/")
async def read_item(item_id: str, repository: ItemRepository = Depends(get_item_repository)):
    item = repository.read(ObjectId(item_id))
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@router.put("/items/{item_id}/")
async def update_item(item_id: str, item: Item, repository: ItemRepository = Depends(get_item_repository)):
    if not repository.update(ObjectId(item_id), item):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated successfully"}


@router.delete("/items/{item_id}/")
async def delete_item(item_id: str, repository: ItemRepository = Depends(get_item_repository)):
    if not repository.delete(ObjectId(item_id)):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
