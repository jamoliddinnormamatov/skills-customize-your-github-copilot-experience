from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# In-memory "database"
items: List[Item] = [
    Item(id=1, name="Sample Item", description="This is a sample item."),
]


@app.get("/items", response_model=List[Item])
def list_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    # simple check to avoid duplicate ids in this starter
    if any(it.id == item.id for it in items):
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    items.append(item)
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for i, it in enumerate(items):
        if it.id == item_id:
            items.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
