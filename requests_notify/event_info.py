import requests
import json
import re

# return json representation of event from given url
def get_event_info(url):
    info = requests.post(url, json={})
    return info.json()

# return an array of json objects w/ price and seat availability for event where price is <= threshold
def get_cheap_tickets(event_json, threshold):
    items = event_json["Items"]
    seats = list()
    for item in items:
        price_str = ""
        max_price = 0
        if (item["PriceWithFees"] != None and item["PriceWithFees"] != ""):
            price = get_price(item["Price"])
            price_fees = get_price(item["PriceWithFees"])
            if (price > price_fees):
                price_str = item["Price"]
                max_price = price
            else:
                price_str = item["PriceWithFees"]
                max_price = price_fees
        else:
           max_price =  get_price(item["Price"])
           price_str = item["Price"]
        
        if (max_price <= threshold):
            ticket = {"Price" : price_str, "Section" : item["Section"], "Row" : item["Row"], 
                      "Quantity Range" : item["QuantityRange"]}
            seats.append(ticket)
    return seats

# return numeric representation of the price
def get_price(price_str):
    nums = re.findall(r'\d+', price_str)
    res = 0
    if (len(nums) > 1):
        fact = 1
        i = len(nums) - 1
        while i >= 0:
            res += int(int(nums[i])*fact)
            fact *= 1000
            i -= 1
    else:
        res += int(nums[0])
    # if (res >= 1000): print(price_str)
    return res

url0 = "https://www.stubhub.ca/iron-maiden-vancouver-tickets-10-2-2023/event/151714575/"
url1 = "https://www.stubhub.ca/boston-celtics-boston-tickets-5-9-2023/event/151513495/"
url2 = "https://www.stubhub.ca/guns-n-roses-vancouver-tickets-10-16-2023/event/151494664/"

# example calls

# info0 = get_event_info(url0)
# info1 = get_event_info(url1)
info2 = get_event_info(url2)
print(info2["Items"])
# print(info2.keys())
# print(info0["Items"][0].keys())

# print(info0["Items"][0]["Price"])
# print(get_price(info0["Items"][0]["Price"]))

# for item in info0["Items"]:
#     print(item["PriceWithFees"])
# print(get_price('330'))
# print(get_price("1,200"))
# print(get_price("C$1,234,654"))
# print(get_price("C$12,345"))

# tix1 = get_cheap_tickets(info1, 3500)
tix2 = get_cheap_tickets(info2, 1200)

# print(tix2)

# for t in tix2:
#     print(t["Price"])