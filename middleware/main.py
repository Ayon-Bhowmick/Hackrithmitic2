from fastapi import FastAPI

api = FastAPI()

@api.get("/ping")
async def ping():
    return "pong"
