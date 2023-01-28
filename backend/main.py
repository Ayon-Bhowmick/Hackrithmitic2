from fastapi import FastAPI, Response, Query
from starlette.responses import StreamingResponse
from routes import *


api = FastAPI()
db = database.getDatatbase()

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

# !change this to get_airport_graph
@api.get(
    "/graph/airport",
    responses = {
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response)
async def get_airport_graph():
    return StreamingResponse(graphs.graphAirlines(), media_type="image/png")

@api.get("/display")
async def getMessageData():
    return database.getMessageData(db)

@api.get("/findbyairline/{airline}")
async def getMsgByAirline(airline: str):
    return database.getMsgByAirline(db, airline)

@api.get("/findbyflight/{flightId}")
async def getMsgByFlight(flightId: str):
    return database.getMsgByFlight(db, flightId)


# Routes
# user to post the message flight numer and phone number
    # insert message, flight#, phone# in user table
# put in your flight number and phone nmber (for subscribers)
    # insert flight#, phone#


# get all post on regular home screen
    # select all from user table ranked by time
# get sort all post for certain airline
    # select all message from feedback where airline id is #
# get find all for certain airport (add airport to table)
    # select all message from feedback where airport id is #
# get find all for a flight number
    # select message from ffeedback table if flight id is #
# erick - get all phone numbers that have the same flight number
    # select phone numbers from user table if flight number is #
# get all the rating of an airline (positive or negative)
    #
#
