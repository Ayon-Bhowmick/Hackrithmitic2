from fastapi import FastAPI, Response
from starlette.responses import StreamingResponse
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
    return StreamingResponse(graphs.graphAirlines(), media_type="image/png")

@api.get(
    "/graph/airport",
    responses = {
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response)
async def get_airport_graph():
    return StreamingResponse(graphs.graphAirports(), media_type="image/png")
