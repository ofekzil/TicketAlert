from run_queries import USERNAME, PASSWORD, ENDPOINT, PORT, DATABASE, insert, delete, select
import mysql.connector
from datetime import datetime, date

e0 = {'performer':'Iron Maiden', 
      'venue':'Rogers Arena, Vancouver, British Columbia',
      'eventDate':'Oct 02 2023',
      'eventUrl':"https://www.stubhub.ca/iron-maiden-vancouver-tickets-10-2-2023/event/151714575/",
      'threshold':160,
      'email':'ticketreciever@yahoo.com'}
e1 = {'performer':"Guns N' Roses", 
      'venue':'BC Place Stadium, Vancouver, British Columbia',
      'eventDate':'Oct 16 2023',
      'eventUrl':"https://www.stubhub.ca/guns-n-roses-vancouver-tickets-10-16-2023/event/151494664/",
      'threshold':140,
      'email':'ticketreciever@yahoo.com'}
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

select()
# insert(novenue)
# delete()
# con = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
# cursor = con.cursor()
# cursor.execute("DELETE FROM EventInfo WHERE eventUrl = 'https://www.stubhub.ca/'")
# cursor.execute("INSERT INTO EventInfo(performer, eventDate, eventUrl, threshold, email) VALUES(%(performer)s, %(eventDate)s, %(eventUrl)s, %(threshold)s, %(email)s)", novenue)
# con.commit()
# cursor.execute("SELECT * FROM EventInfo;")
# for (performer, venue, eventDate, eventUrl, threshold, email) in cursor:
#     print(performer, venue, eventDate, eventUrl, threshold, email)
# for row in cursor.fetchall():
#     print(type(row), row)
# cursor.close()
# con.close()