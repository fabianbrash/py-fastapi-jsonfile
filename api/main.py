from fastapi import FastAPI
import json
import urllib.request

app = FastAPI()
s3 = True

if s3:
    with urllib.request.urlopen("https://s3.amazonaws.com/fb_bin/USD.json") as f:
        s3_data = json.load(f)
else:
    with open("USD.json") as file:
        d = json.load(file)

@app.get("/", tags=["root"])
def read_root() -> dict:
    if s3:
        return {"data": s3_data}
    else:
        return {"data": d}
