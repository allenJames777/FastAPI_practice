from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    item_id: int
    name: str
    price: float

class UpdateItem(BaseModel):
    name: str
    price: float

shopping_list=[]

#SEARCH and GET ITEMS
@app.get("/items")
def get_items(search: str = None, max_price: float = None):
    results = shopping_list
    if search:
        results = [item for item in results if search.lower() in item["name"].lower()]
    if max_price:
        results = [item for item in results if item["price"] <= max_price]
    return {"items": results}

@app.post("/items/")
def add_item(item: Item):
    shopping_list.append({"id": item.item_id, "name": item.name, "price": item.price})
    return {"message": f"Item ID{item.item_id} {item.name} added at ${item.price}"}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    for id in shopping_list:
        if id["id"]== item_id:
            shopping_list.remove(id)
            return {"message":f"Id:{item_id} Item:{id['name']} Removed!"}
    return {"message": f"{item_id} not found"}

@app.put("/items/{item_id}")
def update_item(item_id: int, updated: UpdateItem):
    for item in shopping_list:
        if item["id"] == item_id:
            item["name"] = updated.name
            item["price"] = updated.price
            return {"message": f"Item {item_id} updated!"}
    return {"message": "Item not found"}