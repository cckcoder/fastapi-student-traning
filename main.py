from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routers import icecreams
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")

origins = [
    "*",
    "http://localhost",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
