import psycopg2
import json
 
DB_NAME = "pdmyimse"
DB_USER = "pdmyimse"
DB_PASS = "jXzVyAlo_BZgjHU5rk7gR66BD7Y_2Y4l"
DB_HOST = "raja.db.elephantsql.com"
DB_PORT = "5432"
 # postgres://username:password@hostname:port/database
 # postgres://pdmyimse:jXzVyAlo_BZgjHU5rk7gR66BD7Y_2Y4l@raja.db.elephantsql.com/pdmyimse
def getDatatbase():
    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        print("Database connected successfully")
        if (conn == None):
            print("Error: psycopg2.connect() returned a None object")
            return None
        #cursor = conn.cursor()
        #return cursor
        return conn

    except Exception as e:
        print("Database not connected successfully")
        print(e)

    try:
        createAirlineTable = '''CREATE TABLE airlines (
                            id SERIAL PRIMARY KEY,
                            company VARCHAR(255) NOT NULL,
                            flight_number VARCHAR(255) NOT NULL UNIQUE
                            );'''
        createUserTable = '''CREATE TABLE users (
                            id SERIAL PRIMARY KEY,
                            title VARCHAR(255) DEFAULT NULL,
                            message TEXT DEFAULT NULL,
                            flight_number VARCHAR(255) NOT NULL,
                            phonenumber BIGINT,
                            created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                            rating INTEGER,
                            ispositive BOOLEAN,
                            airline_id INTEGER REFERENCES airline(id)
                            );'''
        createRatingTable = '''CREATE TABLE rating (
                            id SERIAL PRIMARY KEY,
                            positive INT,
                            negative INT,
                            company VARCHAR(255) UNIQUE
                            );
                            '''

    except:
        pass

# Get a list of all the feedback
def getMessageData(conn):
    cursor = conn.cursor()
    array = []
    table = {}
    getAllMessage = "SELECT title, message, flight_number, created_at FROM users;"
    cursor.execute(getAllMessage)
    fetch = cursor.fetchall()
    for row in fetch:
        table["title"] = row[0]
        table["message"] = row[1]
        table["flight_number"] = row[2]
        table["created_at"] = row[3].strftime("%Y-%m-%d %H:%M:%S")
        #jObj = json.dumps(table)
        #array.append(jObj)
        array.append(table.copy())
    #fetch = json.dumps(array)
    return array

# /findbyairline
def getMsgByAirline(conn, airline):
    cursor = conn.cursor()
    array = []
    table = {}
    getAllMessage = f'''SELECT DISTINCT title, message, users.flight_number, created_at FROM users 
                    JOIN airlines ON users.airline_id = airlines.id
                    WHERE airlines.company = '{airline}';'''
    cursor.execute(getAllMessage)
    fetch = cursor.fetchall()
    for row in fetch:
        table["title"] = row[0]
        table["message"] = row[1]
        table["flight_number"] = row[2]
        table["created_at"] = row[3].strftime("%Y-%m-%d %H:%M:%S")
        array.append(table.copy())
    return array

def getMsgByFlight(conn, flight):
    cursor = conn.cursor()
    array = []
    table = {}
    getAllMessage = f'''SELECT DISTINCT title, message, users.flight_number, created_at FROM users
                    JOIN airlines ON users.airline_id = airlines.id
                    WHERE users.flight_number = '{flight}';;'''
    cursor.execute(getAllMessage)
    fetch = cursor.fetchall()
    for row in fetch:
        table["title"] = row[0]
        table["message"] = row[1]
        table["flight_number"] = row[2]
        table["created_at"] = row[3].strftime("%Y-%m-%d %H:%M:%S")
        array.append(table.copy())
    return array


def addUser(cursor, user, flight, phoneNumber, mess):
    
    pass

def subscribe(conn, flight, phoneNumber):
    try:
        cursor = conn.cursor()
        sql = f'''INSERT INTO users (flight_number, phonenumber) VALUES (%s, %s);'''
        values = (flight, phoneNumber)
        cursor.execute(sql, values)
        conn.commit()
        return 1
    except Exception as e:
        print(e)


def review(conn, title, message, flightNum, phoneNum, val):
    try:
        cursor = conn.cursor()
        sql = f'''INSERT INTO users (title, message, flight_number, phonenumber, ispositive) VALUES (%s, %s, %s, %s, %s);'''
        values = (title, message, flightNum, phoneNum, val)
        cursor.execute(sql, values)
        conn.commit()
        return 1
    except Exception as e:
        print(e)

def addAirlineInfo(conn, airlineName, flightNum):
    try:
        cursor = conn.cursor()
        sql = f'''INSERT INTO airlines (company, flight_number) VALUES (%s, %s);'''
        values = (airlineName, flightNum)
        cursor.execute(sql, values)
        conn.commit()
        return 1
    except Exception as e:
        print(e)

    
#review(getDatatbase(), "I love delta", "delta gave me free food on the flight", "DL123", 6017918060, True)
#addAirlineInfo(getDatatbase(), "American Airlines", "AA1111")
# Testing
#subscribe(getDatatbase(), "AA1234", 6017918060)
#getPosts(getDatatbase())
#oogieboogie = getMsgByFlight(getDatatbase(), "AA1234")
#print(oogieboogie)

print(getMessageData(getDatatbase()))

