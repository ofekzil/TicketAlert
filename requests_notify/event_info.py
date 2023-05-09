import requests
import json
import re

# class representing an event on StubHub
class Event:

    # values initialized in the constructor will first be part of dummy data used for testing
    # eventually they will be retrieved from a database
    def __init__(self, url, event_date) -> None:
        self.url = url
        self.event_json = self.get_event_info(url)
        self.event_date = event_date


    # return json representation of event from given url
    # can chnage PageSize to control number of returned results
    def get_event_info(self, url):
        info = requests.post(url, json={"SortBy" : "Price", "PageSize" : 50})
        return info.json()
    
    # check if the event has already passed (event datetime < current datetime)
    def is_past(self):
        # TODO
        pass

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
url1 = "https://www.stubhub.ca/boston-celtics-boston-tickets-5-9-2023/event/151513495/"
url2 = "https://www.stubhub.ca/guns-n-roses-vancouver-tickets-10-16-2023/event/151494664/"

# using class

maiden = Event(url0, "Oct 2 2023") # TODO: replace date string w/ Date object (or equivalent)
nba = Event(url1, "May 9 2023")
gnr = Event(url2, "Oct 16 2023")

print(maiden.get_cheap_tickets(175))


# Invalid now, before class was created!!!
# keeping as examples
# info0 = get_event_info(url0)
# info1 = get_event_info(url1)
# info2 = get_event_info(url2)
# print(info2["Items"])
# print(info0.keys())
# print(info0["Quantity"])
# print(info0["Items"][0].keys())
# print(info0["SortDirection"], info0["SortBy"], info0["PageVisitId"], info0["PageSize"])

# print(len(info0["Items"]))
# print(get_price(info0["Items"][0]["Price"]))

# for item in info1["Items"]:
#     print(item["Section"] + " " + item["Row"]+ " " + item["Price"] + " " + item["QuantityRange"])

# print(get_price('330'))
# print(get_price("1,200"))
# print(get_price("C$1,234,654"))
# print(get_price("C$12,345"))

# tix0 = get_cheap_tickets(info0, 100)
# print(tix0)
# print(len(tix0))
# print(len(info1["Items"]))
# tix1 = get_cheap_tickets(info1, 3500)
# print(tix1)
# print(len(tix1))
# tix2 = get_cheap_tickets(info2, 1200)

# print(tix2)

# for t in tix2:
#     print(t["Price"])