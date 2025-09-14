from fastapi import FastAPI

app = FastAPI()

test = {45 : 'apple', 2: 'banana'}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": test.get(item_id)}

@app.get("/items")
def read_items():
    return test

@app.post("/items/{item_id}")
def create_item(item_id: int, name: str):
    test[item_id] = name
    return {"item_id": item_id, "name": name}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    del test[item_id]
    return {"message": "Item deleted"}