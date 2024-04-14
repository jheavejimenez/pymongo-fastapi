from app.core.models import Item
from app.core.repositories import ItemRepository


class MockCollection:
    def __init__(self):
        self.items = {}

    def insert_one(self, item):
        self.items[item.id] = item
        return item.id

    def find_one(self, item_id):
        return self.items.get(item_id)

    def update_one(self, item_id, update_data):
        if item_id in self.items:
            self.items[item_id].update(update_data)
            return True
        return False

    def delete_one(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False


def test_item_repository():
    # Test ItemRepository create, read, update, delete methods
    repository = ItemRepository(MockCollection())

    # Test create method
    item = Item(id="123", name="Test Item", description="Test Description")
    inserted_id = repository.create(item)
    assert inserted_id == "123"

    # Test read method
    retrieved_item = repository.read("123")
    assert retrieved_item.id == "123"
    assert retrieved_item.name == "Test Item"
    assert retrieved_item.description == "Test Description"

    # Test update method
    updated_item = Item(id="123", name="Updated Item", description="Updated Description")
    assert repository.update("123", updated_item)
    updated_item = repository.read("123")
    assert updated_item.name == "Updated Item"
    assert updated_item.description == "Updated Description"

    # Test delete method
    assert repository.delete("123")
