from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int = Field(...)
    name: str = Field(...)


class ItemCreate(BaseModel):
    name: str = Field(...)


class ItemUpdate(BaseModel):
    name: str = Field(...)
