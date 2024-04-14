from typing import Optional

from bson import ObjectId
from pymongo.collection import Collection

from .models import Item


class ItemRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def create(self, item: Item) -> ObjectId:
        data = item.dict()
        new_item = self.collection.insert_one(data)
        created_item = self.collection.find_one({"_id": new_item.inserted_id})
        return created_item

    def read(self, item_id: ObjectId) -> Optional[Item]:
        item_data = self.collection.find_one({"_id": item_id})
        if item_data:
            return Item(**item_data)
        else:
            return None

    def update(self, item_id: ObjectId, item: Item) -> bool:
        data = item.dict()
        result = self.collection.update_one({"_id": item_id}, {"$set": data})
        return result.modified_count == 1

    def delete(self, item_id: ObjectId) -> bool:
        result = self.collection.delete_one({"_id": item_id})
        return result.deleted_count == 1
