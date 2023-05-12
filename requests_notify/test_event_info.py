from event_info import Event
import unittest
from datetime import datetime

# old dummy data
url0 = "https://www.stubhub.ca/iron-maiden-vancouver-tickets-10-2-2023/event/151714575/"
url1 = "https://www.stubhub.ca/boston-celtics-boston-tickets-5-14-2023/event/151513498/"
url2 = "https://www.stubhub.ca/guns-n-roses-vancouver-tickets-10-16-2023/event/151494664/"
maiden = Event(datetime.strptime("Oct 02 2023", "%b %d %Y"), "example@gmail.com")
nba = Event(datetime.strptime("May 14 2023", "%b %d %Y"), "yourEmAiL@yahoo.com")
gnr = Event(datetime.strptime("Oct 16 2023", "%b %d %Y"), "my.email@gmail.com")
past = Event(datetime.strptime("Oct 03 2022", "%b %d %Y"), "AnAddress123@gmail.com")

# common dummy data to all instances and test cases
email = "myEmail123@gmail.com"
performer = "Some Band"
venue = "Arena, City, Province, Country"
date = datetime.strptime("Oct 02 2023", "%b %d %Y")

# object jsons contain only relevant fields needed. 
# Actual data retrived from POST has more attributes that are not necessary right now
no_tix = {"Items" : []}
t1 = {"Items" : [{"Price" : "C$100", "PriceWithFees" : "C$125", "Section":"102", "Row":"14", "QuantityRange" : "1 - 3"},
                 {"Price" : "C$123", "PriceWithFees" : "C$147", "Section":"FLOOR", "Row":"", "QuantityRange" : "1 - 5"},
                 {"Price" : "C$50", "PriceWithFees" : "C$75", "Section":"325", "Row":"10", "QuantityRange" : "1"},
                 {"Price" : "C$260", "PriceWithFees" : "C$285", "Section":"B7", "Row":"2", "QuantityRange" : "1 - 2"}]}
t1_all = [{"Price" : "C$125", "Section" : "102", "Row" :"14", "Quantity Range" : "1 - 3"},
               {"Price" : "C$147", "Section" : "FLOOR", "Row" :"", "Quantity Range" : "1 - 5"},
               {"Price" : "C$75", "Section" : "325", "Row" :"10", "Quantity Range" : "1"},
               {"Price" : "C$285", "Section" : "B7", "Row" :"2", "Quantity Range" : "1 - 2"}]
t1_under130 = [{"Price" : "C$125", "Section" : "102", "Row" :"14", "Quantity Range" : "1 - 3"},
               {"Price" : "C$75", "Section" : "325", "Row" :"10", "Quantity Range" : "1"}]
t2 = {"Items" : [{"Price" : "C$100", "PriceWithFees" : "", "Section":"102", "Row":"14", "QuantityRange" : "1 - 3"},
                 {"Price" : "C$123", "PriceWithFees" : None, "Section":"FLOOR", "Row":"", "QuantityRange" : "1 - 5"},
                 {"Price" : "C$50", "PriceWithFees" : "C$75", "Section":"325", "Row":"10", "QuantityRange" : "1"},
                 {"Price" : "C$260", "PriceWithFees" : "C$285", "Section":"B7", "Row":"2", "QuantityRange" : "1 - 2"}]}
t2_under130 = [{"Price" : "C$100", "Section" : "102", "Row" :"14", "Quantity Range" : "1 - 3"},
               {"Price" : "C$123", "Section" : "FLOOR", "Row" :"", "Quantity Range" : "1 - 5"},
               {"Price" : "C$75", "Section" : "325", "Row" :"10", "Quantity Range" : "1"}]
t1_under130_notify = "Email will be sent to: " + email + ".\nMessage: There are tickets available for " + performer \
                            + " at venue " + venue + " on " + date.strftime("%m/%d/%Y") + " as of " \
                            + datetime.now().strftime("%m/%d/%Y %H:%M:%S") + ". There is no guarantee tickets will still be"\
                            " available after this message is sent.\nThe following are some of the available tickets for you:\n"\
                            + "Price: C$125, Section: 102, Row: 14, Seat Quantity Range: 1 - 3\n" \
                            + "Price: C$75, Section: 325, Row: 10, Seat Quantity Range: 1\n"
t2_under130_notify = "Email will be sent to: " + email + ".\nMessage: There are tickets available for " + performer \
                            + " at venue " + venue + " on " + date.strftime("%m/%d/%Y") + " as of " \
                            + datetime.now().strftime("%m/%d/%Y %H:%M:%S") + ". There is no guarantee tickets will still be"\
                            " available after this message is sent.\nThe following are some of the available tickets for you:\n"\
                            + "Price: C$100, Section: 102, Row: 14, Seat Quantity Range: 1 - 3\n" \
                            + "Price: C$123, Section: FLOOR, Row: , Seat Quantity Range: 1 - 5\n" \
                            + "Price: C$75, Section: 325, Row: 10, Seat Quantity Range: 1\n"

class TestEvent(unittest.TestCase):
    
    def setUp(self) -> None:
        self.e1 = Event(date, email)

    def test_get_price(self):
        self.assertEqual(100, self.e1.get_price("C$100"))
        self.assertEqual(0, self.e1.get_price("C$0"))
        self.assertEqual(1000, self.e1.get_price("C$1,000"))
        self.assertEqual(12345, self.e1.get_price("C$12,345"))
        self.assertEqual(123456789, self.e1.get_price("$123,456,789"))

    def test_get_cheap_tix_no_tix(self):
        self.e1.event_json = no_tix
        self.assertListEqual([], self.e1.get_cheap_tickets(10))

    def test_get_cheap_tickets_none(self):
        self.e1.event_json = t1
        self.assertListEqual([], self.e1.get_cheap_tickets(30))

    def test_get_cheap_tix_partial(self):
        self.e1.event_json = t1
        self.assertListEqual(t1_under130, self.e1.get_cheap_tickets(130))

    def test_get_cheap_tix_partial_no_fees(self):
        self.e1.event_json = t2
        self.assertListEqual(t2_under130, self.e1.get_cheap_tickets(130))

    def test_get_cheap_tix_all(self):
        self.e1.event_json = t1
        self.assertListEqual(t1_all, self.e1.get_cheap_tickets(300))

    def test_notify_tix(self):
        self.assertEqual(t1_under130_notify, self.e1.notify(t1_under130, performer, venue))
        self.assertEqual(t2_under130_notify, self.e1.notify(t2_under130, performer, venue))
    
    def test_notify_no_tix(self):
        self.assertEqual("No tickets below threshold. DO NOT SEND NOTIFICATION!", self.e1.notify([], performer, venue))
    
    def test_is_past(self):
        self.assertFalse(self.e1.is_past())
        self.e1.event_date = datetime.now()
        self.assertFalse(self.e1.is_past())
        self.e1.event_date = datetime.strptime("Oct 02 2022", "%b %d %Y")
        self.assertTrue(self.e1.is_past())