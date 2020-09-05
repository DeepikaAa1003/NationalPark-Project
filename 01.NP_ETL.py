# Dependencies and Setup
import pandas as pd
import numpy as np
import requests
import pymongo
import json
from pprint import pprint
# Importing API key
from api_keys import np_api_key

#Mongo Connection

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

#Database Creation
db = client.NationalParksDB

# Drops parks collection if available to remove duplicates
db.parks.drop()

# open/create parks collection
parks = db.parks

#API Retrieval Process

#Parks Collection insert
park_base_url = "https://developer.nps.gov/api/v1/parks?"

counter = 0
while (counter <= 450):
    with open('parks.json', 'w') as f:   
        park_url= f"{park_base_url}&api_key={np_api_key}&start={counter}"
        response_json = requests.get(park_url).json()
        json.dump(response_json, f)

        park_data = response_json["data"]
    
        for i in park_data:
            parks.insert_one(i)
            print("Data Inserted")
            counter = counter + 1
print(counter)

#### Web Cams Retrieval ####

# Drops parks collection if available to remove duplicates
db.webcams.drop()

# open/create parks collection
webcams = db.webcams

# Web Cams Collection insert
web_cams_url = "https://developer.nps.gov/api/v1/webcams?"

cam_counter = 0
while (cam_counter <= 150):
    with open('webcams.json', 'w') as g:   
        cam_url= f"{web_cams_url}&api_key={np_api_key}&start={cam_counter}"
        cam_response_json = requests.get(cam_url).json()
        json.dump(cam_response_json, g)

        cam_data = cam_response_json["data"]
    
        for cam in cam_data:
            webcams.insert_one(cam)
            print("CamData Inserted")
            cam_counter = cam_counter + 1
print(cam_counter)
