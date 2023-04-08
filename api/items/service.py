import os
from supabase import create_client
from fastapi import status
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")


class ItemService:
    def __init__(self):
        client = create_client(url, key)
        self.db = client.table("items")

    def index(self):
        try:
            items = self.db.select("id", "name").execute()
            return items.data
        except Exception as e:
            logger.exception(e)
            raise

    def show(self, id):
        try:
            item = self.db.select("id", "name").eq("id", id).execute()
            return item.data[0]
        except Exception as e:
            logger.exception(e)
            raise

    def create(self, item):
        try:
            self.db.insert(item).execute()
            return JSONResponse(
                status_code=status.HTTP_201_CREATED, content={"msg": "Created"}
            )
        except Exception as e:
            logger.exception(e)
            raise

    def update(self, id, item):
        try:
            self.db.update(item).eq("id", id).execute()
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={})
        except Exception as e:
            logger.exception(e)
            raise

    def delete(self, id):
        try:
            self.db.delete().eq("id", id).execute()
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={})
        except Exception as e:
            logger.exception(e)
            raise
