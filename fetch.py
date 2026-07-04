# this file will be for calling the api and sending it sql
import requests 
import os
from dotenv import load_dotenv 
import mysql.connector

load_dotenv()
apikey = os.getenv('FINNHUB_API_KEY')


params = {"symbol": "MGNI", "token": apikey)
url = "https://finhub.io/api/v1/quote"

response = requests.get(url, params=params)

data = response.json()
price = data("c")
print (price)

everything = {
  "symbol": "MGNI",
  "price" : data["c"],
  "high": data["h"],
  "low": data["l"],
  "prev_close": data["pc"]
}
