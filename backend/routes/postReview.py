import requests
import os

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


#print(getAirline(input("Flight Number: ")))
