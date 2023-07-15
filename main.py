from fastapi import FastAPI

from modules import models

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello World!"
    }


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {
        "item_id": item_id,
    }


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


@app.get("/models/{model_name}")
async def get_model(model_name: models.ModelName):
    return models.get_model(model_name)


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {
        "file_path": file_path
    }
