from app.core.models import Item


def test_item_model():
    # Test Item model creation and attributes
    item = Item(id="123", name="Test Item", description="Test Description")
    assert item.id == "123"
    assert item.name == "Test Item"
    assert item.description == "Test Description"
