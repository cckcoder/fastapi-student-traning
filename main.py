from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return { 'message': 'Hello World'}


@app.get("/ice_cream/{id}")
def read_ice_cream(
    id: int, q: Optional[str] = None
):
    return { 'ice_cream_id': id, 'q': q } 
    
