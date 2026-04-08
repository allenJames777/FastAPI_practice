from fastapi import FastAPI

app=FastAPI()
shopping_list=[]

@app.get("/")
def home():
    return {"message": "Welcome to Shopping List API"}

@app.get("/items")
def about():
    return {"items": shopping_list}

@app.post("/items/{item_name}/{price}")
def add_item(item_name:str,price:float):
    shopping_list.append({"name":item_name,"price":price })
    return{"message": f"Item:{item_name} added, Price:{price}"}

@app.delete("/items/{item_name}/price")
def delete_item(item_name:str):
    for item in shopping_list:
        if item["name"] == item_name:
            shopping_list.remove(item)
            return {"message":f"{item_name} Removed!"}
    return{"message":f"{item_name} not found"}

@app.put("/items/{new_item}/{new_price}")
def update_item(new_item:str,new_price:float):
    for item in shopping_list:
        if item["name"] == new_item:
            item["price"] = new_price
            return {"message": f"{new_item} price updated to ${new_price}"}
    return {"message": f"{new_item} not found"}    
