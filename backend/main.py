from fastapi import FastAPI, Response
from routes import *


api = FastAPI()

@api.get("/ping")
async def ping():
    return "pong"

@api.get(
    "/graph/airline",
    responses = {
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response)
async def get_airline_graph():
    return Response(content=graphs.graphAirlines(), media_type="image/png")
