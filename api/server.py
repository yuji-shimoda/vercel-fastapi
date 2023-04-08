from fastapi import FastAPI
from api.items.views import router as items_router

app = FastAPI()
app.include_router(items_router, prefix="/items", tags=["Items"])
