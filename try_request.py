import requests
import json

# url = 'https://www.stubhub.ca/Browse/VenueMap/GetSvgDataSh/151714575?categoryId=4093&withFees=true'
# url = "https://www.stubhub.ca/philadelphia-76ers-philadelphia-tickets-8-6-2023/event/151513543"
url = "https://www.stubhub.ca/iron-maiden-vancouver-tickets-10-2-2023/event/151714575/"
myobj = json.load(open("./headers.json"))

x = requests.post(url, json = {})

#print(type(x))
#print(x.text)
# print(x.json().keys())
j = x.json()
print(j)
