from fastapi import FastAPI, Response
from routes import *


api = FastAPI()

@api.get("/ping")
async def ping():
    return "pong"

@api.get("/graph/airline")
async def get_airline_graph():
    return Response(content=image_bytes, media_type="image/png")
