import psycopg2
 
DB_NAME = "pdmyimse"
DB_USER = "pdmyimse"
DB_PASS = "jXzVyAlo_BZgjHU5rk7gR66BD7Y_2Y4l"
DB_HOST = "raja.db.elephantsql.com"
DB_PORT = "5432"
 # postgres://username:password@hostname:port/database
 # postgres://pdmyimse:jXzVyAlo_BZgjHU5rk7gR66BD7Y_2Y4l@raja.db.elephantsql.com/pdmyimse
try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
    cursor = conn.cursor()
    airlineTable = '''CREATE TABLE airline (
                id SERIAL PRIMARY KEY,
                company VARCHAR(255) NOT NULL
                );'''
    cursor.execute(airlineTable)
    conn.commit()
    findVal = '''SELECT company FROM airline;'''
    cursor.execute(findVal)
    fetch = cursor.fetchall()
    print(fetch)
    #cursor.execute('''INSERT INTO airline (company) VALUES ('Spirit Airlines');''')


except Exception as e:
    print("Database not connected successfully")
    print(e)

