from fastapi import FastAPI
from routers import icecreams

app = FastAPI()

app.include_router(icecreams.router)

@app.get("/")
async def hello_world():
    return { 'message': 'Hello World'}
