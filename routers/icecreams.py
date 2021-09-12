import os, shutil
from starlette.requests import Request

from models.ice_cream_model import IceCreamPydantic, IceCreamPydanticIn, IceCream
from auth.basic_auth import get_current_username

from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, Response, status


BASE_PATH = os.path.abspath(os.curdir)
STATIC_DIR = os.path.join(BASE_PATH, 'static')

async def save_file(picture):
    with open(f'{STATIC_DIR}/{picture.filename}', 'wb') as buffer:
        try:
            shutil.copyfileobj(picture.file, buffer)
        except Exception as e:
            print(e)


router = APIRouter(prefix="/ice_cream", tags=["ice_cream"])


@router.get("/")
async def get_all_ice_cream(username: str = Depends(get_current_username)):
    __import__("pprint").pprint(username)
    return await IceCreamPydantic.from_queryset(IceCream.all().order_by("-id"))


@router.get("/{id}")
async def read_ice_cream(id: int, q: Optional[str] = None):
    return await IceCreamPydantic.from_queryset_single(IceCream.get(id=id))


@router.post("/", response_model=IceCreamPydantic)
async def create_ice_cream(ice_cream: IceCreamPydanticIn):
    ice_cream_obj = await IceCream.create(**ice_cream.dict(exclude_unset=True))
    return await IceCreamPydantic.from_tortoise_orm(ice_cream_obj)

@router.post("/image")
async def upload_file(request: Request, response: Response):
    form_data = await request.form()
    picture = form_data.get('picture')
    await save_file(picture)
    response.status_code = status.HTTP_201_CREATED
    return { 'message': 'upload image successful'}



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
