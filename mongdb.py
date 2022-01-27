from pymongo import MongoClient
import json
# pprint library is used to make the output look more pretty
#from pprint import pprint

def insertJsonFile(jsonFilePath):
    client = MongoClient("mongodb+srv://aarab99:DQhyeXSn5m93zJvA@cluster0.mqn9a.mongodb.net/scrapingDB?retryWrites=true&w=majority")
    # print("\n\n\nClient == ",client)
    db = client["scrapingDB"]
    # db.drop_collection("cryptosTest")
    collection = db.create_collection("cryptosTest")

    with open(jsonFilePath) as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    if isinstance(jsonObject, list):
        collection.drop()

        collection.insert_many(jsonObject)
    else:
        collection.insert_one(jsonObject)
        
    

