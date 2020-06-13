import requests
import json

apiKey = 'b8ec178c-b211-48ea-be2f-7191e988efb7' # Your api key. Enter /api new on mc.hypixel.net.

merchantPrices = json.loads(open('merchantPrices.json', 'r').read())

def _fetch(url):
    return (lambda u: requests.get(url).json())(url)

def fetchPriceData(itemName):
    statdata = _fetch("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey)
    return {'sellPrice' : statdata['products'][itemName]['quick_status']['sellPrice'], 'buyPrice' : statdata['products'][itemName]['quick_status']['buyPrice']}

def fetchAllItems():
    

