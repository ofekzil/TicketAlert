from run_queries import insert, USERNAME, PASSWORD, ENDPOINT, PORT, DATABASE
import mysql.connector

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
        'eventUrl':'https://ww.stubhub.ca/',
        'threshold':75,
        'email':'someEmail@mail.com'}

insert(e1)

con = mysql.connector.connect(user=USERNAME, password=PASSWORD, host=ENDPOINT, port=PORT, database=DATABASE)
cursor = con.cursor()
cursor.execute("SELECT * FROM EventInfo;")
for (performer, venue, eventDate, eventUrl, threshold, email) in cursor:
    print(performer, venue, eventDate, eventUrl, threshold, email)
cursor.close()
con.close()