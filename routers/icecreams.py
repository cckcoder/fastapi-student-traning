from typing import Optional
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class IceCream(BaseModel):
    id: int
    flavor: str
    price: float
    is_active: Optional[bool] = None

router = APIRouter(
    prefix="/ice_cream",
    tags=["ice_cream"]
)

ice_creams_db = [
  {
    "id": 1,
    "flavor": "Vanilla",
    "price": 59,
    "is_active": True
  },
  {
    "id": 2,
    "flavor": "Chocolate",
    "price": 59,
    "is_active": True
  },
  {
    "id": 3,
    "flavor": "Mint Chocolate Chip",
    "price": 69,
    "is_active": True
  }
]


@router.get("/")
async def get_all_ice_cream():
    return ice_creams_db 


@router.get("/{id}")
async def read_ice_cream(id: int, q: Optional[str] = None):
    ice_cream = ice_creams_db[id - 1]
    return ice_cream


@router.post("/", response_model=IceCream)
async def create_ice_cream(ice_cream: IceCream):
    ice_creams_db.append(jsonable_encoder(ice_cream))
    return ice_cream


@router.put("/{id}")
async def update_ice_cream(id: int, ice_cream: IceCream):
    return { 
        "flavor": ice_cream.flavor 
        ,"id": id
    }


@router.delete("/{id}")
async def delete_ice_cream(id: int):
    icc_cream = ice_creams_db[id - 1]
    ice_creams_db.pop(id - 1)
    message = f"The flavor {icc_cream.get('flavor')} get delete!"
    return message
