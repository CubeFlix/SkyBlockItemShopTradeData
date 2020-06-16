#!python3
#
# A image gatherer for Hypixel Skyblock item icons.
# By Kevin Chen

from bs4 import BeautifulSoup
import requests
import json
import os
import shutil

def saveImage(fileName, url):
    r = requests.get(url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True
    
    with open(fileName,'wb') as f:
        shutil.copyfileobj(r.raw, f)

os.chdir("..")

exceptions = {"LOG" : "Oak_Wood",
"LOG:1" : "Spruce_Wood",
"LOG:2" : "Birch_Wood",
"LOG_2:1" : "Dark_Oak_Wood",
"LOG_2" : "Acacia_Wood",
"LOG:3" : "Jungle_Wood",
"RAW_FISH:1" : "Raw_Salmon",
"RAW_FISH:3" : "Pufferfish",
"INK_SACK:4" : "Lapis_Lazuli",
"INK_SACK:3" : "Cocoa_Beans"}

for itemName in json.loads(open("merchantPrices.json", mode='r').read()):
    if itemName in exceptions:
        itemName = exceptions[itemName]
    soup = BeautifulSoup(requests.get("https://hypixel-skyblock.fandom.com/wiki/"+itemName.title()).text, 'html.parser')
    image = soup.findAll("img", {"class": "pi-image-thumbnail"})
    if len(image) > 1:
        for img in range(len(image)):
            saveImage("img/icons/"+itemName+str(img)+".png", image[img]['src'])
            print("Downloading image: "+ "https://hypixel-skyblock.fandom.com/wiki/"+itemName.title())
    else:
        for img in image:
            saveImage("img/icons/"+itemName+".png", img['src'])
            print("Downloading image: "+ "https://hypixel-skyblock.fandom.com/wiki/"+itemName.title())

