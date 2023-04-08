from fastapi import APIRouter
from api.items.service import ItemService
from api.items.models import Item, ItemCreate, ItemUpdate
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter()


@router.get("", response_model=list[Item])
async def list_items():
    return ItemService().index()


@router.get("/{id}", response_model=Item)
async def show_item(id: int):
    return ItemService().show(id)


@router.post("")
async def create_item(item: ItemCreate):
    return ItemService().create(item.dict())


@router.patch("/{id}")
async def update_item(id: int, item: ItemUpdate):
    return ItemService().update(id, item.dict())


@router.delete("/{id}")
async def delete_item(id: int):
    return ItemService().delete(id)
