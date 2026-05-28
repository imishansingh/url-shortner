import random
import string

from fastapi import FastAPI

app = FastAPI()

url_store = {}

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.post("/shorten")
def shorten_url(url: str):
    code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    url_store[code] = url
    return {"short_code": code, "original_url": url}

@app.get("/{short_code}")
def redirect_url(short_code: str):
    original = url_store.get(short_code)
    if not original:
        return {"error": "URL not found"}
    return {"original_url": original}
