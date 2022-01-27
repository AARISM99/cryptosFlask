import time
from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime
from scraping_coinmarketcup import lancerScraping

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "http://localhost:4200"}})

csvFilePath = "crypto_data.csv"
jsonFilePath = "crypto_data.json"

@app.route("/")
def hello():   
    return "Hello, World!"

@app.route("/lancerScraping")
def scraping() :
    start_time = time.time()   
    # time.sleep(60)
    lancerScraping(int(request.args.get("nbre_pages")))
    hours: int = time.gmtime(time.time() - start_time).tm_hour
    minutes: int = time.gmtime(time.time() - start_time).tm_min
    seconds: int = time.gmtime(time.time() - start_time).tm_sec
    fin_time = ""
    if(hours !=0) : fin_time += str(hours) + 'h ' 
    if(minutes !=0): fin_time += str(minutes) + 'm '  
    if(seconds !=0): fin_time += str(seconds) + 's'
    print("\n\ntime of scraping = " + fin_time)
    return jsonify({'time': fin_time,'date': datetime.datetime.now()})

# @app.route("/save")
# def saveJsonFileInMongoDB() :
#     insertJsonFile(jsonFilePath)
#     return "save file successfully"


# @app.route("/data")
# def showData():
#     with open(jsonFilePath) as jsonFile:
#         jsonObject = json.load(jsonFile)
#         jsonFile.close()
        
#     return {"data": jsonObject}


