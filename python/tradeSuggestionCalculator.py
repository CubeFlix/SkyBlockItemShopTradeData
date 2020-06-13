#!python3
#
# Bazaar prices and item shop prices are often different, so we can exploit that.
# This tool will get all trades where the user can profit from these price differences.
# By Kevin Chen

import requests
import json

#todo: port to html with item shop values, make video

apiKey = 'b8ec178c-b211-48ea-be2f-7191e988efb7' # Your api key. Enter /api new on mc.hypixel.net.

merchantPrices = json.loads(open('merchantPrices.json', 'r').read())
idExceptions = json.loads(open('itemNameExceptions.json', mode='r').read())


def _fetch(url):
    return (lambda u: requests.get(url).json())(url)

def fetchPriceData(itemName):
    statdata = _fetch("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey)
    return {'sellPrice' : statdata['products'][itemName]['quick_status']['sellPrice'], 'buyPrice' : statdata['products'][itemName]['quick_status']['buyPrice']}

def calculateTrade(itemName):
    itemPrices = fetchPriceData(itemName)
    
    if itemPrices['sellPrice'] > merchantPrices[itemName]['price']:
        return {'item' : itemName, 'type' : 'sellToBazaar', 'bazaarSellPrice' : itemPrices['sellPrice'], 'merchantPrice' : merchantPrices[itemName]['price'],
                'netGain' : itemPrices['sellPrice'] - merchantPrices[itemName]['price'], 'merchantName' : merchantPrices[itemName]['merchantName']}
    else:
        return None

def getAllTrades():
    finaltrades = []
    for item in merchantPrices:
        if calculateTrade(item) != None:
            finaltrades.append(calculateTrade(item))
    return finaltrades

def parseName(name):
    if name in idExceptions:
        return idExceptions[name]
    else:
        return name

def sortByNetGain(trades):
    return sorted(trades, reverse=True, key=lambda elem : elem['netGain'])

def returnAllTrades():
    finaltrades = getAllTrades()
    finaltrades = sortByNetGain(finaltrades)
    for trade in finaltrades:
        print("Trade: " + "Sell " + parseName(trade['item']).replace('_', ' ').title() + ' from item shop at a price of ' + str(trade['merchantPrice']) + ' coins to the bazaar at ' + str(trade['bazaarSellPrice']) + ' coins for a net gain of ' + str(trade['netGain']) + ' coins each.')
        
    

if __name__ == "__main__":
    returnAllTrades()


    

