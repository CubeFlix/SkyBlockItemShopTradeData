#!python3
#
# This tool will get all price data for the item shops.

import requests
import json

idExceptions = json.loads(open('itemNameExceptions.json', 'r').read())
itemData = json.loads(open('merchantPrices.json', 'r').read())

def fetchData(itemName):
    return itemData[itemName]

def parseName(name):
    if name in idExceptions:
        return idExceptions[name]
    else:
        return name

if __name__ == "__main__":
    for item in itemData:
        print("Item: "+parseName(item).replace('_', ' ').title() +"  " + "Price: "+str(itemData[item]['price']))
    

