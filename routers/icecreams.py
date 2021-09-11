from models.ice_cream_model import IceCreamPydantic, IceCreamPydanticIn, IceCream
from auth.basic_auth import get_current_username

from typing import Optional
from fastapi import APIRouter, HTTPException, Depends

from typing import Optional
from fastapi import APIRouter, HTTPException


router = APIRouter(prefix="/ice_cream", tags=["ice_cream"])

ice_creams_db = [
    {"id": 1, "flavor": "Vanilla", "price": 59, "is_active": True},
    {"id": 2, "flavor": "Chocolate", "price": 59, "is_active": True},
    {"id": 3, "flavor": "Mint Chocolate Chip", "price": 69, "is_active": True},
]


@router.get("/")
async def get_all_ice_cream():
    return await IceCreamPydantic.from_queryset(IceCream.all().order_by("-id"))


@router.get("/{id}")
async def read_ice_cream(id: int, q: Optional[str] = None):
    ice_cream = ice_creams_db[id - 1]
    return ice_cream


@router.post("/", response_model=IceCreamPydantic)
async def create_ice_cream(ice_cream: IceCreamPydanticIn):
    ice_cream = await IceCream.create(**ice_cream.dict(exclude_unset=True))
    return await IceCreamPydantic.from_tortoise_orm(ice_cream)


@router.put("/{id}")
async def update_ice_cream(id: int, ice_cream: IceCreamPydanticIn):
    await IceCream.filter(id=id).update(**ice_cream.dict(exclude_unset=True))
    return await IceCreamPydantic.from_queryset_single(IceCream.get(id=id))


@router.delete("/{id}")
async def delete_ice_cream(id: int):
    is_delete = await IceCream.filter(id=id).delete()
    if not is_delete:
        raise HTTPException(status_code=404, detail=f"Ice cream id: {id} not found")
    return {"message": f"Ice cream id: {id} deleted"}
