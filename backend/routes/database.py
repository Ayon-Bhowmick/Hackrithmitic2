import psycopg2
import os
import json

DB_NAME = "pdmyimse"
# DB_NAME = os.environ["DB_NAME"]
DB_USER = "pdmyimse"
# DB_USER = os.environ["DB_NAME"]
DB_PASS = "jXzVyAlo_BZgjHU5rk7gR66BD7Y_2Y4l"
# DB_PASS = os.environ["DB_PASS"]
DB_HOST = "raja.db.elephantsql.com"
# DB_HOST = os.environ["DB_HOST"]
# DB_PORT = os.environ["DB_PORT"]
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
    getAllMessage = "SELECT title, message, flight_number, created_at FROM users WHERE message IS NOT NULL;"
    cursor.execute(getAllMessage)
    fetch = cursor.fetchall()
    for row in fetch:
        table["title"] = row[0]
        table["message"] = row[1]
        table["flight_number"] = row[2]
        table["created_at"] = row[3].strftime("%Y-%m-%d %H:%M:%S")
        array.append(table.copy())
    return array

# /findbyairline
def getMsgByAirline(conn, airline):
    cursor = conn.cursor()
    array = []
    table = {}
    getAllMessage = f'''SELECT title, message, users.flight_number, created_at FROM users
                    JOIN airlines ON users.flight_number = airlines.flight_number
                    WHERE message IS NOT NULL AND airlines.company = '{airline}';'''
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
    getAllMessage = f'''SELECT title, message, flight_number, created_at FROM users
                    WHERE flight_number = '{flight}' AND message IS NOT NULL;'''
    cursor.execute(getAllMessage)
    fetch = cursor.fetchall()
    for row in fetch:
        table["title"] = row[0]
        table["message"] = row[1]
        table["flight_number"] = row[2]
        table["created_at"] = row[3].strftime("%Y-%m-%d %H:%M:%S")
        array.append(table.copy())
    return array

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
    cursor = conn.cursor()
    sql = f"""SELECT * FROM airlines WHERE flight_number = '{flightNum}'"""
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    if(result == []):
        sql = f'''INSERT INTO airlines (company, flight_number) VALUES (%s, %s);'''
        values = (airlineName, flightNum)
        cursor.execute(sql, values)
        conn.commit()
        return 1


def ratingsJsonObj(conn):
    cursor = conn.cursor()
    sql = f'''SELECT DISTINCT company FROM airlines;'''
    cursor.execute(sql)
    airlines = cursor.fetchall()

    for i in airlines:
        sql = f'''SELECT COUNT(*) FROM users
                WHERE ispositive = true
                AND flight_number IN (SELECT flight_number FROM airlines WHERE company = '{i[0]}');'''
        cursor.execute(sql)
        posRes = cursor.fetchone()

        sql = f'''SELECT COUNT(*) FROM users
                WHERE ispositive = false
                AND flight_number IN (SELECT flight_number FROM airlines WHERE company = '{i[0]}');'''
        cursor.execute(sql)
        negRes = cursor.fetchone()

        sql = f'''SELECT COUNT(*) FROM rating WHERE company = '{i[0]}';'''
        cursor.execute(sql)
        result = cursor.fetchone()

        if (result[0] == 1):
            sql = f'''UPDATE rating
                    SET positive = {posRes[0]}, negative = {negRes[0]}
                    WHERE company = '{i[0]}';'''
            cursor.execute(sql)
            conn.commit()
        else:
            sql = f'''INSERT INTO rating (positive, negative, company)
                    VALUES ({posRes[0]}, {negRes[0]}, '{i[0]}');'''
            cursor.execute(sql)
            conn.commit()
    sql = f'''SELECT company, positive, negative FROM rating;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    array = []
    table = {}
    for i in result:
        table["company"] = i[0]
        table["positive"] = i[1]
        table["negative"] = i[2]
        array.append(table.copy())
    return array

def hasFlightNumber(conn, flight_number):
    cursor = conn.cursor()
    sql = f'''SELECT flight_number FROM users WHERE flight_number = '{flight_number}';'''
    cursor.execute(sql)
    result = cursor.fetchall()
    if result != None:
        return True
    else:
        return False

def fetchPhoneNumber(conn, flight_number):
    cursor = conn.cursor()
    sql = f'''SELECT DISTINCT phonenumber FROM users WHERE flight_number = '{flight_number}';'''
    cursor.execute(sql)
    result = cursor.fetchall()
    arr = []
    for i in result:
        arr.append(i[0])
    return arr

# fetchPhoneNumber(getDatatbase(), "AA1234")
#review(getDatatbase(), "I love delta", "delta gave me free food on the flight", "DL123", 6017918060, True)
#addAirlineInfo(getDatatbase(), "American Airlines", "AA1111")
# Testing
#subscribe(getDatatbase(), "AA1234", 6017918060)
#getPosts(getDatatbase())
#oogieboogie = getMsgByFlight(getDatatbase(), "AA1234")
#print(oogieboogie)
# addAirlineInfo(getDatatbase(), "Delta", "DL7234")
#print(getMessageData(getDatatbase()))
