import requests
import json
import re

url0 = "https://www.stubhub.ca/iron-maiden-vancouver-tickets-10-2-2023/event/151714575/"
url1 = "https://www.stubhub.ca/philadelphia-76ers-philadelphia-tickets-8-6-2023/event/151513543"
# myobj = json.load(open("./headers.json")) #not needed as arg for POST request

# return json representation of event from given url
def get_event_info(url):
    info = requests.post(url, json={})
    return info.json()

# example call
info0 = get_event_info(url0)
# print(info0["Items"][0].keys())


# returnan array of json objects w/ price and seat availability for event where price is <= threshold
def get_cheap_tickets(event_json, threshold):
    items = event_json["Items"]
    seats = list()
    for item in items:
        price = 0
        price_str = ""
        if (item["PriceWithFees"] != None):
            if (get_price(item["Price"]) > get_price(item["PriceWithFees"])):
                price = get_price(item["Price"])
                price_str = item["Price"]
            else:
                price = get_price(item["PriceWithFees"])
                price_str = item["PriceWithFees"]
        else:
           price =  get_price(item["Price"])
        
        if (price <= threshold):
            ticket = {"Price" : price_str, "Section" : item["Section"], "Row" : item["Row"], "Quantity Range" : item["QuantityRange"]}
            seats.append(ticket)
    return seats

# return numeric representation of the price
def get_price(price_str):
    return int(re.findall(r'\d+', price_str)[0])

print(info0["Items"][0]["Price"])
print(get_price(info0["Items"][0]["Price"]))

print(get_cheap_tickets(info0, 175))