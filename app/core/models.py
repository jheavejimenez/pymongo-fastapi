from pydantic import BaseModel, Field
from bson import ObjectId


class Item(BaseModel):
    id: ObjectId = Field(description="item id")
    name: str = Field(...)
    description: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
