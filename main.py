from typing import Union
from fastapi import FastAPI

from modules import models
from db import fake_items

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello World!"
    }


@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items.fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:  # ?short={True|true|1|on|yes}
        item.update({
            "description": "This is an amazing super item that has a long description"
        })
    return item


@app.get("/users/me")
async def read_user_me():
    return {
        "user_id": "the current user",
        "name": "fakecurrentuser"
    }


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {
        "user_id": user_id,
        "name": "fakeuser"
    }


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: str, item_id: int, q: Union[str, None] = None):
    return {
        "user_id": user_id,
        "item_id": item_id,
        "q": q
    }


@app.get("/models/{model_name}")
async def get_model(model_name: models.ModelName):
    return models.get_model(model_name)


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {
        "file_path": file_path
    }
