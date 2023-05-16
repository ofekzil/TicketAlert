import mysql.connector
import os
from event_info import Event 

USERNAME = os.environ.get("USERNAME") 
PASSWORD = os.environ.get("PASSWORD")
ENDPOINT = os.environ.get("ENDPOINT")
PORT = os.environ.get("PORT")
DATABASE = os.environ.get("DATABASE")

def connect_to_db():
    try:
        db_conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
        print(db_conn)
        # cursor = db_conn.cursor()
        return db_conn
    except mysql.connector.Error as e:
        print(e)

def disconnect_from_db():
    global cursor, db_conn
    # cursor.close()
    db_conn.close()

def create_event_table():
    db_conn =  mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
    with open('./requests_notify/sql/create.sql', 'r') as sql:
        with db_conn.cursor() as cursor:
            cursor.execute(sql.read(), multi=True)
    db_conn.commit()
    c = db_conn.cursor()
    c.execute("select table_name from information_schema.tables;")
    db_conn.close()


con = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT)
cursor = con.cursor()
cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='TicketAlert_DB' AND `TABLE_NAME`='EventInfo';")
for row in cursor:
    print(row)

cursor.close()
con.close()


# cursor.execute("SELECT CURDATE();")

# for row in cursor:
#     print(row)

# create_event_table()
# conn = connect_to_db()
# conn.cursor().execute("select table_name from information_schema.tables;")
# disconnect_from_db()
