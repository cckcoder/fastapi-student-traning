from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class IceCream(BaseModel):
    flavor: str
    price: float
    is_active: Optional[bool] = None


@app.get("/")
async def hello_world():
    return { 'message': 'Hello World'}


@app.get("/ice_cream/{id}")
async def read_ice_cream(
    id: int, q: Optional[str] = None
):
    return { 'ice_cream_id': id, 'q': q } 
    

@app.put("/ice_cream/{id}")
async def update_flavor(id: int, ice_cream: IceCream):
    return { 
        "flavor": ice_cream.flavor 
        ,"id": id
    }
