import mysql.connector
import os
from event_info import Event 
from datetime import datetime

USERNAME = os.environ.get("USERNAME") 
PASSWORD = os.environ.get("PASSWORD")
ENDPOINT = os.environ.get("ENDPOINT")
PORT = os.environ.get("PORT")
DATABASE = os.environ.get("DATABASE")

DATE_FORMAT = "%b %d %Y"

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

# function to create the EventInfo table from create.sql file
def create_event_table():
    try:
        db_conn =  mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
        with open('./requests_notify/sql/create.sql', 'r') as sql:
            with db_conn.cursor() as cursor:
                cursor.execute(sql.read(), multi=True)
        db_conn.commit()
        db_conn.close()
    except mysql.connector.Error as e:
        print(e)

# insert data into EventInfo table
# info_json is a dict of format {'performer' : str, 'venue':str, 'eventDate':str, 'eventUrl':str(url), 'threshold':int, 'email':str}
# info_json will be given from caller (i.e. client side)
# must convert eventDate to datetime object
def insert(info_json):
    info_json["eventDate"] = datetime.strptime(info_json["eventDate"], DATE_FORMAT)
    try:
        db_conn =  mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
    except mysql.connector.Error as e:
        print(e)
    
    cursor = db_conn.cursor()
    try:
        cursor.execute("INSERT INTO EventInfo VALUES(%(performer)s, %(venue)s, %(eventDate)s, %(eventUrl)s, %(threshold)s, %(email)s)", info_json)
    except mysql.connector.IntegrityError as e:
        print("Duplicate value inserted. Error: {}".format(e))
    
    db_conn.commit()
    cursor.close()
    db_conn.close()

# delete all past events from the database, dates whose date has already passed
def delete():
    try:
        db_conn =  mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
    except mysql.connector.Error as e:
        print(e)
    
    cursor = db_conn.cursor()

    cursor.execute("DELETE FROM EventInfo WHERE eventDate < DATE(NOW());")
    db_conn.commit()
    cursor.close()
    db_conn.close()

