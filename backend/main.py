from fastapi import FastAPI, Response, Query, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse
from routes import *





api = FastAPI()
db = database.getDatatbase()


api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/ping")
async def ping():
    return "pong"

@api.get(
    "/graph",
    responses = {
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response)
async def get_airline_graph():
    return StreamingResponse(graphs.graphAirlines(), media_type="image/png")

@api.get("/display")
async def getMessageData():
    return database.getMessageData(db)

@api.get("/findbyairline")
async def getMsgByAirline(airline: str = Body(..., embed=True)):
    return database.getMsgByAirline(db, airline)

@api.get("/findbyflight")
async def getMsgByFlight(flight_number: str = Body(..., embed=True)):

    return database.getMsgByFlight(db, flight_number)

@api.post("/postreview")
async def reviewFlight(flight_number: str = Body(...), message: str = Body(...), title: str = Body(...), phonenumber: str = Body(...)):
    airline = postReview.getAirline(flight_number)
    database.addAirlineInfo(db, airline, flight_number)

    trueFalseVal = postReview.getSentiment(message)
    val = database.review(db, title, message, flight_number, phonenumber, trueFalseVal)

    if val == 1: # if added succesffuly, check phone number
        # twilio here
        # if flight number already exist in the table, select all the numbers with the same flight number
        send_text.send_text_msg()
        return {
            "message": "Review added successfully"
        }



    #except:
    #    raise HTTPException(status_code=400, detail="Error adding user to the database")



@api.post("/subscribe")
async def subscribeToFlight(flight_number: str = Body(...), phonenumber: str = Body(...)):

    try:
        res = database.subscribe(db, flight_number, phonenumber)
        if (res == 1):
            return {
                "message":"User added succesfully"
            }
    except:
        raise HTTPException(status_code=400, detail="Error adding user to the database")


#@api.delete("/unsubscribe")


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
