import psycopg2
 
DB_NAME = "pdmyimse"
DB_USER = "pdmyimse"
DB_PASS = "jXzVyAlo_BZgjHU5rk7gR66BD7Y_2Y4l"
DB_HOST = "postgres://pdmyimse:jXzVyAlo_BZgjHU5rk7gR66BD7Y_2Y4l@raja.db.elephantsql.com/pdmyimse"
DB_PORT = "5432"
 
try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
except:
    print("Database not connected successfully")