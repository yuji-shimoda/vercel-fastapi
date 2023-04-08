from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def read_hello():
    return {"msg": "Hello World"}
