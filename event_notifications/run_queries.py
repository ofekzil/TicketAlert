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

DATE_FORMAT = "%m %d %Y"

PERFORMER_IDX = 0
DATE_IDX = 1
URL_IDX = 2
THRESHOLD_IDX = 3
EMAIL_IDX = 4

SENDER = os.environ.get("SENDER")

UNSUBSCRIBE_API = "https://kq9m75lhb3.execute-api.us-west-1.amazonaws.com/test/unsubscribe"

ses_client = boto3.client("ses")

# sends verification email to given email address
# sends the default AWS verification email, NOT a custom one
def verify_email(email):
    response = ses_client.verify_email_identity(EmailAddress=email)
    print(response)

# check if given email address is verified
def is_verified(email):
    res = ses_client.get_identity_verification_attributes(Identities=[email])
    return email in res["VerificationAttributes"] and res["VerificationAttributes"][email]["VerificationStatus"] == "Success"

# send ticket notification to email using Amazon SES
def send_notification(notification, email, performance, threshold, url):
    if (notification != "No tickets below threshold. DO NOT SEND NOTIFICATION!"):
        response = ses_client.send_email(
            Source=SENDER,
            Destination={"ToAddresses":[email]},
            Message={
                "Body":{
                    "Html" : {"Data" : "<html><body><p>"+notification.replace("\n", "<br>")+"</p> <br>"
                                        + "<footer> <a href='" + url + "'>event page url</a><br>"
                                        + "<a href='" + UNSUBSCRIBE_API + "?url=" + url + "&threshold=" + str(threshold)
                                        + "&email=" + email + "'>click here to unsubscribe from notifications for this event</a>"
                                        +"</footer></body></html>", 
                                "Charset" : "UTF-8"},
                    "Text" : {"Data" : (notification), "Charset" : "UTF-8"}
                },
                "Subject":{
                    "Data":"Notification for Available Tickets for: " + performance,
                    "Charset":"UTF-8"
                }
            }        
        )
        print(response)

# sends unsubscription notification when event has passed
def send_unsubscribe_notification(email, performance, date):
    notification = "This email is a notification that you will no longer receive notifications of tickets for " \
                    + performance + " on " + date.strftime("%m/%d/%Y") + ", as the event has already passed as of " \
                    + datetime.now().strftime("%m/%d/%Y") + ".\nThank you for using this service for your ticket notifications!"
    response = ses_client.send_email(Source=SENDER,
                                    Destination={"ToAddresses":[email]},
                                    Message={
                                        "Body":{
                                            "Text" : {"Data" : (notification), "Charset" : "UTF-8"},
                                        },
                                        "Subject":{
                                            "Data":"Expiry of Ticket Alert Notifications",
                                            "Charset":"UTF-8"
                                        }
                                    }        
                                )
    print(response)

# function to create the EventInfo table from create.sql file
def create_event_table():
    try:
        db_conn =  mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
        with open('./event_notifications/sql/create.sql', 'r') as sql:
            with db_conn.cursor() as cursor:
                cursor.execute(sql.read(), multi=True)
        db_conn.commit()
        db_conn.close()
    except mysql.connector.Error as e:
        print(e)

# insert data into EventInfo table
# info_json is a dict of format {'performerAndCity' : str, 'eventDate':str of form (Mon(int) Date(int) Year(int)), 
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
        cursor.execute("INSERT INTO EventInfo VALUES(%(performerAndCity)s, %(eventDate)s, %(eventUrl)s, %(threshold)s, %(email)s)", info_json)
        db_conn.commit()
        # UNCOMMENT below line to send email notifications. It's commented out so messages aren't sent when not needed
        # verify_email(info_json["email"])
    except mysql.connector.IntegrityError as e:
        print("Duplicate value inserted. Error: {}".format(e))
    

    cursor.execute("SELECT * FROM EventInfo")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db_conn.close()

# find all past events from the database (ones whose date has already passed), send unsubscription notification 
# and delete from DB
def delete():
    try:
        db_conn =  mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
    except mysql.connector.Error as e:
        print(e)
    
    cursor = db_conn.cursor()

    # UNCOMMENT below lines to send unsubscription notifications. Commented out so messages aren't wasted
    # cursor.execute("SELECT email, performerAndCity, eventDate FROM EventInfo WHERE eventDate < DATE(NOW())")
    # for row in cursor.fetchall():
    #     send_unsubscribe_notification(row[0], row[1], row[2])

    cursor.execute("DELETE FROM EventInfo WHERE eventDate < DATE(NOW());")
    db_conn.commit()
    cursor.execute("SELECT * FROM EventInfo")
    for row in cursor.fetchall():
        print(row)
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
    cursor.execute("SELECT performerAndCity, eventDate, eventUrl, threshold, email "\
                    "FROM EventInfo WHERE eventDate >= DATE(NOW())")
    rows = cursor.fetchall()

    # tuples are of order (performer, venue, eventDate, eventUrl, threshold, email), same as rows in DB, including null values
    for row in rows:
        print(row[PERFORMER_IDX])
        if (is_verified(row[EMAIL_IDX])):
            event = Event((datetime(datetime.now().year, 12, 31) if row[DATE_IDX] == None else row[DATE_IDX]), row[EMAIL_IDX])
            if (event.get_event_info(row[URL_IDX])):
                cheap_tix = event.get_cheap_tickets(row[THRESHOLD_IDX])
                notification = event.notify(cheap_tix, ("Performer" if row[PERFORMER_IDX] == None else row[PERFORMER_IDX]))
                print(notification)
                # UNCOMMENT below line to send email notifications. It's commented out so messages aren't sent when not needed
                # send_notification(notification, row[EMAIL_IDX], "Performance" if row[PERFORMER_IDX] == None else row[PERFORMER_IDX],
                #                   row[THRESHOLD_IDX], row[URL_IDX])
        else:
            print("email not verified")
    
    cursor.close()
    db_conn.close()

# deletes row w/ given key from database, which will ensure no future emails are sent to this person for this event and threhsold
def unsubscribe(url, threshold, email):
    try:
        db_conn =  mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
    except mysql.connector.Error as e:
        print(e)
    
    cursor = db_conn.cursor()
    cursor.execute("DELETE FROM EventInfo WHERE eventUrl=%(url)s AND threshold=%(threshold)s AND email=%(email)s",
                   {"url" : url, "threshold" : threshold, "email" : email})
    db_conn.commit()
    cursor.close()
    db_conn.close()
    print("Unsubscription successful!")
