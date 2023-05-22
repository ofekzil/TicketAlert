from run_queries import USERNAME, PASSWORD, ENDPOINT, PORT, DATABASE, SENDER, insert, delete, select, send_notification, create_event_table
import mysql.connector
from datetime import datetime, date
import os

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

# create_event_table()
# print(RECEIVER)
#send_notification("I have some tickets available", RECEIVER)
# select()
# insert(e0_new)
# insert(e1_new)
# insert(rockville)
# delete()
# select()
# con = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
# cursor = con.cursor()
# cursor.execute("ALTER TABLE EventInfo RENAME EventInfoOld")
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