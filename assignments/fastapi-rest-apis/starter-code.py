from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# TODO: Define your Pydantic models here
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: str = None

# In-memory data storage (replace with a database in production)
items_db = []

# TODO: Add your endpoints here
# Example GET endpoint:
# @app.get("/items")
# def get_items():
#     return items_db

# Example POST endpoint:
# @app.post("/items")
# def create_item(item: Item):
#     items_db.append(item)
#     return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
