from run_queries import USERNAME, PASSWORD, ENDPOINT, PORT, DATABASE, SENDER, insert, delete, select, send_notification, create_event_table
import mysql.connector
from datetime import datetime, date
import os
import time

RECEIVER = os.environ.get("RECEIVER")

# for EventInfoOld
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

# for EventInfo (most current)
e0_new = {'performerAndCity':'Iron Maiden Vancouver', 
      'eventDate':'10 2 2023',
      'eventUrl':"https://www.stubhub.ca/iron-maiden-vancouver-tickets-10-2-2023/event/151714575/",
      'threshold':160,
      'email':RECEIVER}
e1_new = {'performerAndCity':"Guns N Roses Vancouver", 
      'eventDate':'10 16 2023',
      'eventUrl':"https://www.stubhub.ca/guns-n-roses-vancouver-tickets-10-16-2023/event/151494664/",
      'threshold':140,
      'email':RECEIVER}
past_new = {'performerAndCity':"Some Artist City",
        'eventDate':"8 13 2020",
        'eventUrl':'https://www.stubhub.ca/',
        'threshold':75,
        'email':'someEmail@mail.com'}
rockville = {'performerAndCity':"Welcome To Rockville Daytona Beach", 
      'eventDate':'5 22 2023',
      'eventUrl':"https://www.stubhub.ca/welcome-to-rockville-daytona-beach-tickets-5-18-2023/event/150456734/",
      'threshold':100,
      'email':RECEIVER}

alice = {'performerAndCity':'Alice Cooper Detroit', 
      'eventDate':'5 21 2023',
      'eventUrl':"https://www.stubhub.ca/alice-cooper-detroit-tickets-5-21-2023/event/132569874/",
      'threshold':60,
      'email':RECEIVER}
e1_new_2 = {'performerAndCity':"Guns N Roses Vancouver", 
      'eventDate':'10 16 2023',
      'eventUrl':"https://www.stubhub.ca/guns-n-roses-vancouver-tickets-10-16-2023/event/151494664/",
      'threshold':20,
      'email':RECEIVER}

# t0 = time.time()
# select()
# t1 = time.time()
# print(t1 - t0)
# insert(past_new)
# create_event_table()
# print(RECEIVER)
#send_notification("I have some tickets available", RECEIVER)
# select()
# insert(e1_new_2)
# insert(alice)
# insert(rockville)
# delete()
# select()
# con = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
# cursor = con.cursor()
# cursor.execute("UPDATE EventInfo SET email = 'ticketalertreceiver@gmail.com'")
# cursor.execute("INSERT INTO EventInfo(performer, eventDate, eventUrl, threshold, email) VALUES(%(performer)s, %(eventDate)s, %(eventUrl)s, %(threshold)s, %(email)s)", novenue)
# cursor.execute("DELETE FROM EventInfo WHERE performerAndCity = 'Welcome To Rockville Daytona Beach'")
# con.commit()
# cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'TicketAlert_DB';")
# cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'TicketAlert_DB' AND table_name='EventInfoOld';")
# cursor.execute("SELECT * FROM EventInfo")

# for row in cursor.fetchall():
#     print(row)
# cursor.close()
# con.close()