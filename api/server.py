from fastapi import FastAPI, APIRouter
from api.hello.views import router as hello_router

app = FastAPI()
api_router = APIRouter()
api_router.include_router(hello_router, prefix="/hello", tags=["Hello"])


@app.get("/")
async def read_root():
    return {"msg": "root"}


app.include_router(api_router)
