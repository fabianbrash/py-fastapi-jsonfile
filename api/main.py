from fastapi import FastAPI
import json

app = FastAPI()

with open("USD.json") as file:
    d = json.load(file)

@app.get("/", tags=["root"])
def read_root() -> dict:
    return {"data": d}
