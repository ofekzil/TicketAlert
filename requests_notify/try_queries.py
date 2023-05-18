from run_queries import USERNAME, PASSWORD, ENDPOINT, PORT, DATABASE, SENDER, insert, delete, select, send_notification
import mysql.connector
from datetime import datetime, date
import os

RECEIVER = os.environ.get("RECEIVER")

e0 = {'performer':'Iron Maiden', 
      'venue':'Rogers Arena, Vancouver, British Columbia',
      'eventDate':'Oct 02 2023',
      'eventUrl':"https://www.stubhub.ca/iron-maiden-vancouver-tickets-10-2-2023/event/151714575/",
      'threshold':160,
      'email':RECEIVER}
e1 = {'performer':"Guns N' Roses", 
      'venue':'BC Place Stadium, Vancouver, British Columbia',
      'eventDate':'Oct 16 2023',
      'eventUrl':"https://www.stubhub.ca/guns-n-roses-vancouver-tickets-10-16-2023/event/151494664/",
      'threshold':140,
      'email':RECEIVER}
past = {'performer':"Some Artist",
        'venue':'Arena, City, Province',
        'eventDate':"Aug 13 2020",
        'eventUrl':'https://www.stubhub.ca/',
        'threshold':75,
        'email':'someEmail@mail.com'}
nullvenue = {'performer':"Some Artist",
        'venue':None,
        'eventDate':"Aug 13 2023",
        'eventUrl':'https://www.stubhub.ca/',
        'threshold':60,
        'email':'someEmail@gmail.com'}
novenue = {'performer':"Some Artist",
        'eventDate':"Aug 13 2023",
        'eventUrl':'https://www.stubhub.ca/',
        'threshold':45,
        'email':'someEmail@gmail.com'}

# print(RECEIVER)
#send_notification("I have some tickets available", RECEIVER)
# select()
# insert(novenue)
# delete()
# con = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
# cursor = con.cursor()
# cursor.execute("UPDATE EventInfo SET email = 'ticketalertreceiver@gmail.com'")
# cursor.execute("INSERT INTO EventInfo(performer, eventDate, eventUrl, threshold, email) VALUES(%(performer)s, %(eventDate)s, %(eventUrl)s, %(threshold)s, %(email)s)", novenue)
# con.commit()
# cursor.execute("SELECT * FROM EventInfo;")
# for (performer, venue, eventDate, eventUrl, threshold, email) in cursor:
#     print(performer, venue, eventDate, eventUrl, threshold, email)
# for row in cursor.fetchall():
#     print(type(row), row)
# cursor.close()
# con.close()