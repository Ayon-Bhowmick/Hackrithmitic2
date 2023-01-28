from fastapi import FastAPI, Response
from routes import *


api = FastAPI()

@api.get("/ping")
async def ping():
    return "pong"

<<<<<<< HEAD
=======
@api.get("/graph/airline")
async def get_airline_graph():
    return Response(content=image_bytes, media_type="image/png")
>>>>>>> fb6a14e849a7b24a0201fd1f668df98043d6d956
