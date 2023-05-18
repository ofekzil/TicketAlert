import mysql.connector
import os
from event_info import Event 
from datetime import datetime
import boto3

USERNAME = os.environ.get("USERNAME") 
PASSWORD = os.environ.get("PASSWORD")
ENDPOINT = os.environ.get("ENDPOINT")
PORT = os.environ.get("PORT")
DATABASE = os.environ.get("DATABASE")

DATE_FORMAT = "%b %d %Y"

PERFORMER_IDX = 0
VENUE_IDX = 1
DATE_IDX = 2
URL_IDX = 3
THRESHOLD_IDX = 4
EMAIL_IDX = 5

SENDER = os.environ.get("SENDER")
client = boto3.client("ses")

# send notification to email using Amazon SES
def send_notification(notification, email):
    if (notification != "No tickets below threshold. DO NOT SEND NOTIFICATION!"):
        response = client.send_email(
            Source=SENDER,
            Destination={"ToAddresses":[email]},
            Message={
                "Body":{
                    "Text" : {"Data" : (notification), "Charset" : "UTF-8"},
                },
                "Subject":{
                    "Data":"Notification for Available Tickets",
                    "Charset":"UTF-8"
                }
            }        
        )
        print(response)

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
# info_json is a dict of format {'performer' : str, 'venue':str, 'eventDate':str or form (Mon Date(int) Year(int)), 
#                                 'eventUrl':str(url), 'threshold':int, 'email':str}
# info_json will be given from caller (i.e. client side)
# must convert eventDate to datetime object
def insert(info_json):
    info_json["eventDate"] = datetime.strptime(info_json["eventDate"], DATE_FORMAT)
    try:
        db_conn = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
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

# selects all future events, gets cheap tickets and sends notification to user
# if there is no date provided, default to end of current year
def select():
    try:
        db_conn =  mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
    except mysql.connector.Error as e:
        print(e)
    
    cursor = db_conn.cursor()
    cursor.execute("SELECT performer, venue, eventDate, eventUrl, threshold, email "\
                    "FROM EventInfo WHERE eventDate >= DATE(NOW())")
    rows = cursor.fetchall()

    # tuples are of order (performer, venue, eventDate, eventUrl, threshold, email), same as rows in DB, including null values
    for row in rows:
        event = Event((datetime(datetime.now().year, 12, 31) if row[DATE_IDX] == None else row[DATE_IDX]), row[EMAIL_IDX])
        event.get_event_info(row[URL_IDX])
        cheap_tix = event.get_cheap_tickets(row[THRESHOLD_IDX])
        notification = event.notify(cheap_tix, ("Performer" if row[PERFORMER_IDX] == None else row[PERFORMER_IDX]), 
                     ("Venue" if row[VENUE_IDX] == None else row[VENUE_IDX]))
        print(notification)
        # send_notification(notification, row[EMAIL_IDX])
    cursor.close()
    db_conn.close()
    
    

