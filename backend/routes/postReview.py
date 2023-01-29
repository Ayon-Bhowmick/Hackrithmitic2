import requests
import os
import cohere
from cohere.classify import Example

def getAirline(flightNumber) -> str:
    map = {
        "AA": "American Airlines",
        "2G": "CargoItalia",
        "CO": "Continental Airlines",
        "DL": "Delta Air Lines",
        "NW": "Northwest Airlines",
        "AC": "Air Canada",
        "UA": "United Airlines",
        "CP": "Canadian Airlines",
        "LH": "Lufthansa",
        "FX": "FedEx",
        "AS": "Alaska Airlines",
        "US": "US Airways",
        "RG": "VARIG Brazilian Airlines",
        "KA": "Dragonair",
        "LA": "LAN Airlines",
        "TP": "TAP Air Portugal",
        "CY": "Cyprus Airways",
        "OA": "Olympic Airlines",
        "EI": "Aer Lingus",
        "AZ": "Alitalia",
        "AF": "Air France",
        "IC": "Indian Airlines",
        "HM": "Air Seychelles",
        "OK": "Czech Airlines",
        "SV": "Saudi Arabian Airlines",
        "RB": "Syrian Arab Airlines",
        "ET": "Ethiopian Airlines",
        "GF": "Gulf Air",
        "KL": "KLM Royal Dutch Airlines",
        "IB": "Iberia Airlines",
        "AI": "Air India",
        "BA": "British Airways",
        "EK": "Emirates",
        "BW": "Caribbean Airlines",
        "JL": "Japan Airlines",
        "QR": "Qatar Airways",
        "CX": "Cathay Pacific",
        "EK": "Emirates",
        "WN": "Southwest Airlines",
        "9W": "Jet Airways",
        "LX": "Swiss Air Lines",
        "QT": "TAM Airlines",
        "OH": "Comair",
        "VS": "Virgin Atlantic Airways"
    }
    code = flightNumber[:2]
    return map[code]

def getSentiment(review):
    co = cohere.Client("qjXHW7uXtFQR6Nz5Qml8L2oODO7CYUMxksGN331r")
    classifications = co.classify(
        model='large',
        inputs=[review],
        examples=[Example("The order came 5 days early", "positive"), 
                  Example("The item exceeded my expectations", "positive"), 
                  Example("I ordered more for my friends", "positive"), 
                  Example("I would buy this again", "positive"), 
                  Example("I would recommend this to others", "positive"), 
                  Example("The package was damaged", "negative"), 
                  Example("The order is 5 days late", "negative"), 
                  Example("The order was incorrect", "negative"), 
                  Example("I want to return my item", "negative"), 
                  Example("The item\'s material feels low quality", "negative")])
    print(classifications.classifications)


print(getSentiment(input()))
