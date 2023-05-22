import requests
import json
import re
from datetime import datetime 

# class representing an event on StubHub
class Event:

    # values initialized in the constructor will first be part of dummy data used for testing
    # eventually they will be retrieved from a database

    # might make the constructor parameter a string and turn it into a date here, or keep it as a date 
    # dependent on how info is stored in database
    # also note that not all event dates may have the exact same format, leading to some confusing formatting potentially 
    # possibly only look at date, no time
    def __init__(self, event_date, email) -> None:
        self.event_json = {}
        self.event_date = event_date
        self.email = email


    # return json representation of event from given url
    # can change PageSize to control number of returned results 
    # method will be tested in integration, not unit tests
    # TODO: If event is past, info.url != url, which may be useful for later
    #       In that case tehre may also not be a json attribute available 
    def get_event_info(self, url):
        info = requests.post(url, json={"SortBy" : "Price", "PageSize" : 50})
        if (info.url == url):
            self.event_json = info.json()
            return True
        else:
            return False
    
    # check if the event has already passed (event datetime < current datetime)
    # in future filtering may be done when selecting from DB, and not necessarily here, but will keep function for now
    def is_past(self):
        return datetime.now() > self.event_date

    # return numeric representation of the price
    def get_price(self, price_str):
        nums = re.findall(r'\d+', price_str)
        res = 0
        if (len(nums) > 1):
            fact = 1
            i = len(nums) - 1
            while (i >= 0):
                res += int(int(nums[i])*fact)
                fact *= 1000
                i -= 1
        else:
            res += int(nums[0])
        return res
    
    def get_price_from_seat(self, seat):
        return self.get_price(seat["Price"])

    # return an array of json objects w/ price and seat availability for event where price is <= threshold
    def get_cheap_tickets(self, threshold):
        items = self.event_json["Items"]
        seats = list()
        for item in items:
            price_str = ""
            max_price = 0
            if (item["PriceWithFees"] != None and item["PriceWithFees"] != ""):
                price = self.get_price(item["Price"])
                price_fees = self.get_price(item["PriceWithFees"])
                if (price > price_fees):
                    price_str = item["Price"]
                    max_price = price
                else:
                    price_str = item["PriceWithFees"]
                    max_price = price_fees
            else:
                max_price =  self.get_price(item["Price"])
                price_str = item["Price"]
            
            if (max_price <= threshold):
                ticket = {"Price" : price_str, "Section" : item["Section"], "Row" : item["Row"], 
                        "Quantity Range" : item["QuantityRange"]}
                seats.append(ticket)
        seats.sort(key=self.get_price_from_seat)
        return seats
    
    # construct message for email notification using info in cheap_tickets, performer and venue
    # performer and venue will be kept in DB and retrieved directly from HTML
    def notify(self, cheap_tickets, performance):
        if (len(cheap_tickets) == 0):
            return "No tickets below threshold. DO NOT SEND NOTIFICATION!"
        else:
            notification = "\nThere are tickets available for " + performance \
                            + " on " + self.event_date.strftime("%m/%d/%Y") + " as of " \
                            + datetime.now().strftime("%m/%d/%Y %H:%M:%S") + ". There is no guarantee tickets will still be"\
                            " available after this message is sent.\nThe following are some of the available tickets for you:\n\n"
            for t in cheap_tickets:
                notification += "Price: " + t["Price"] + ", Section: " + t["Section"] + ", Row: " + t["Row"] + ", Seat Quantity Range: " + t["Quantity Range"] + "\n"
            return notification