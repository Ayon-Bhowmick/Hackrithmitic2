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
        cursor = conn.cursor()
        return cursor

    except Exception as e:
        print("Database not connected successfully")
        print(e)

    try:
        createAirlineTable = '''CREATE TABLE airlines (
                            id SERIAL PRIMARY KEY,
                            airport VARCHAR(255) NOT NULL,
                            company VARCHAR(255) NOT NULL,
                            flight_number VARCHAR(255) NOT NULL
                            );'''
        createUserTable = '''CREATE TABLE users (
                            id SERIAL PRIMARY KEY,
                            message VARCHAR(255) NOT NULL,
                            flight_number VARCHAR(255) NOT NULL,
                            phonenumber BIGINT,
                            created_at TIMESTAMP NOT NULL DEFAULT NOW()
                            rating INTEGER,
                            ispositive BOOLEAN;
                            airline_id INTEGER REFERENCES airline(id);
                            );'''
        createRatingTable = '''CREATE TABLE rating (
                            id SERIAL PRIMARY KEY,
                            positive INT,
                            negative INT,
                            company VARCHAR(255) UNIQUE
                            );
                            '''
        insertNewFlight = '''INSERT INTO airline (flight_number, airport, company)
                        VALUES ('AA9999', 'JFK', 'American Airlines');'''
        
        
        #cursor.execute('''INSERT INTO airline (company) VALUES ('Spirit Airlines');''')

    except:
        pass

# Get a list of all the feedback
def getMessageData(cursor):
    array = []
    table = {}
    getAllMessage = "SELECT message, flight_number, created_at FROM users;"
    cursor.execute(getAllMessage)
    fetch = cursor.fetchall()
    for row in fetch:
        table["message"] = row[0]
        table["flight_number"] = row[1]
        table["created_at"] = row[2].strftime("%Y-%m-%d %H:%M:%S")
        #jObj = json.dumps(table)
        #array.append(jObj)
        array.append(table)
    
    #fetch = json.dumps(array)
    print(array)
    return array

def getMsgByAirport():
    pass

def getMsgByAirline():
    pass

def getMsgByFlight():
    pass

#getPosts(getDatatbase())
