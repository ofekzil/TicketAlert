from run_queries import *
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
# send_notification("I have some tickets available", RECEIVER, "")
# select()
# insert(e1_new)
# insert(alice)
# insert(rockville)
# delete()
# select()
# unsubscribe(7)
# insert(e1_new_2)
# con = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
# cursor = con.cursor()
# cursor.execute("ALTER TABLE EventInfo RENAME EventInfoNoId")
# cursor.execute("INSERT INTO EventInfo(performer, eventDate, eventUrl, threshold, email) VALUES(%(performer)s, %(eventDate)s, %(eventUrl)s, %(threshold)s, %(email)s)", novenue)
# cursor.execute("DELETE FROM EventInfo WHERE performerAndCity = 'Welcome To Rockville Daytona Beach'")
# cursor.execute("DROP TABLE EventInfo")
# con.commit()
# cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'TicketAlert_DB';")
# cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'TicketAlert_DB' AND table_name='EventInfo';")
# cursor.execute("SELECT * FROM EventInfo")

# for row in cursor.fetchall():
#     print(row)

# cursor.close()
# con.close()

# create_verification_template()

# print(ses_client.get_custom_verification_email_template(TemplateName="TicketEmailVerification"))

# verify_email(RECEIVER)
# print(ses_client.verify_email_identity(EmailAddress=RECEIVER))

# ids = ses_client.list_identities(IdentityType="EmailAddress")
# print(ids)
# print(ses_client.get_identity_verification_attributes(Identities=ids["Identities"]))

# print(is_verified(RECEIVER))
# print(is_verified(SENDER))
# print(is_verified("someEmail@outlook.ca"))

# send_unsubscribe_notification(RECEIVER, "Iron Maiden Vancouver", datetime.strptime("10 2 2023", DATE_FORMAT))
