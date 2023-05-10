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
    def __init__(self, url, event_date, email) -> None:
        self.url = url
        self.event_json = self.get_event_info(url)
        self.event_date = event_date
        self.email = email


    # return json representation of event from given url
    # can chnage PageSize to control number of returned results
    def get_event_info(self, url):
        info = requests.post(url, json={"SortBy" : "Price", "PageSize" : 50})
        return info.json()
    
    # check if the event has already passed (event datetime < current datetime)
    # in future filtering may be done when selecting from DB, and not necessarily here, but will keep function for now
    def is_past(self):
        return datetime.now() > self.event_date

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
        return seats

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
    
    # construct message for email notification using info in cheap_tickets
    def notify(self, cheap_tickets):
        # TODO
        pass

# example calls
# TODO: create unit tests to test functionality w/ dummy data (not necessarily from POST request)

url0 = "https://www.stubhub.ca/iron-maiden-vancouver-tickets-10-2-2023/event/151714575/"
url1 = "https://www.stubhub.ca/boston-celtics-boston-tickets-5-14-2023/event/151513498/"
url2 = "https://www.stubhub.ca/guns-n-roses-vancouver-tickets-10-16-2023/event/151494664/"

# using class

maiden = Event(url0, datetime.strptime("Oct 02 Mon 07:30PM 2023", "%b %d %a %I:%M%p %Y"), "example@gmail.com")
nba = Event(url1, datetime.strptime("May 14 2023", "%b %d %Y"))
gnr = Event(url2, datetime.strptime("Oct 16 Mon 06:30PM 2023", "%b %d %a %I:%M%p %Y"), "my.email@gmail.com")
past = Event(url0, datetime.strptime("Oct 03 Mon 05:30PM 2022", "%b %d %a %I:%M%p %Y"), "AnAddress123@gmail.com")

# print(maiden.get_cheap_tickets(175))
# print(maiden.event_date)
# print(nba.event_date)
# print(gnr.event_date)
# print(maiden.is_past())
# print(nba.is_past())
# print(gnr.is_past())
# print(past.is_past())
# print(gnr.event_json["Items"][0]["HasBestValue"])
# for item in maiden.event_json["Items"]:
#     if item["HasBestValue"]:
#         print(item)