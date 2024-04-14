from collections.abc import Collection
from unittest.mock import patch

from bson import ObjectId
from fastapi.testclient import TestClient

from app.core.models import Item
from app.core.repositories import ItemRepository
from app.main import create_app


def test_create_item():
    # Mock repository
    class MockRepository(ItemRepository):
        def __init__(self, collection: Collection):
            super().__init__(collection)
            self.collection = collection

        def create(self, item: Item) -> ObjectId:
            return ObjectId(b'foo-bar-quux')  # Return a fixed ID for testing

    # Patch the get_item_repository function to return the mock repository
    with patch('app.core.database.get_item_repository', return_value=MockRepository):
        # Create a test FastAPI app
        app = create_app()

        # Create a test client
        client = TestClient(app)

        # Test creating an item
        response = client.post("/items/", json={"name": "Test Item", "description": "Test Description"})
        assert response.status_code == 200
        assert response.json() == {"id": "666f6f2d6261722d71757578"}


def test_read_item():
    # Mock repository
    class MockRepository(ItemRepository):
        def __init__(self, collection: Collection):
            super().__init__(collection)
            self.collection = collection

        def read(self, item_id: str) -> Item:
            return Item(id=item_id, name="Test Item", description="Test Description")

    # Patch the get_item_repository function to return the mock repository
    with patch('app.core.database.get_item_repository', return_value=MockRepository):
        # Create a test FastAPI app
        app = create_app()

        # Create a test client
        client = TestClient(app)

        # Test reading an item
        response = client.get("/items/666f6f2d6261722d71757578/")
        assert response.status_code == 200
        assert response.json() == {"id": "666f6f2d6261722d71757578", "name": "Test Item", "description": "Test Description"}
