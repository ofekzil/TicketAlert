import mysql.connector
import os

USERNAME = os.environ.get("DB_USERNAME") 
PASSWORD = os.environ.get("DB_PASSWORD")
ENDPOINT = os.environ.get("ENDPOINT")
PORT = os.environ.get("PORT")

db_conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT)
print(db_conn)

cursor = db_conn.cursor()
cursor.execute("SELECT CURDATE();")

for row in cursor:
    print(row)

cursor.close()
db_conn.close()