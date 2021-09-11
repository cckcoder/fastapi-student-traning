from fastapi import FastAPI
from routers import icecreams
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

app.include_router(icecreams.router)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models.ice_cream_model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
