from pymongo import MongoClient

from app.core.repositories import ItemRepository


def get_item_repository() -> ItemRepository:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["testdb"]
    collection = db["testcollection"]
    return ItemRepository(collection)
