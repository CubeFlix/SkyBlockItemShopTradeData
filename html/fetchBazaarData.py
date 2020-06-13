#!python3
#
# This tool will get all price data for the bazaar.

import requests
import json

idExceptions = json.loads(open('itemNameExceptions.json', mode='r').read())

def fetch(url):
    return (lambda u: requests.get(url).json())(url)

def fetchPriceData(itemName):
    statdata = fetch("https://api.hypixel.net/skyblock/bazaar?key=b8ec178c-b211-48ea-be2f-7191e988efb7")
    return {'sellPrice' : statdata['products'][itemName]['quick_status']['sellPrice'], 'buyPrice' : statdata['products'][itemName]['quick_status']['buyPrice']}

def fetchData(itemName):
    return fetch("https://api.hypixel.net/skyblock/bazaar?key=b8ec178c-b211-48ea-be2f-7191e988efb7")

statdata = fetch("https://api.hypixel.net/skyblock/bazaar?key=b8ec178c-b211-48ea-be2f-7191e988efb7")

data = requests.get("https://api.hypixel.net/skyblock/bazaar/products?key=b8ec178c-b211-48ea-be2f-7191e988efb7").json()

def parseName(name):
    if name in idExceptions:
        return idExceptions[name]
    else:
        return name

if __name__ == "__main__":
    for item_name in data.get("productIds"):
        print("Item: "+parseName(statdata['products'][item_name]['quick_status']['productId']).replace('_', ' ').title() +"  " + "Sell Price: "+str(statdata['products'][item_name]['quick_status']['sellPrice'])+"  " + "Buy Price: "+str(statdata['products'][item_name]['quick_status']['buyPrice']))
    

