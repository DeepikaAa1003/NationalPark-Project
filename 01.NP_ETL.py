# Dependencies and Setup
import pandas as pd
import numpy as np
import requests
import pymongo
from pprint import pprint
# Importing API key
from api_keys import np_api_key

#Mongo Connection

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Database Creation
db = client.NationalParksDB

# Drops collection if available to remove duplicates
db.parks.drop()

# open the specific collection
parks = db.parks

#API Retrieval
park_base_url = "https://developer.nps.gov/api/v1/parks?"
park_url= f"{park_base_url}&api_key={np_api_key}"
park_url

pages = list(range(0, 496))
pages_list = pages[0:496:50]

for page in pages_list:
    park_url= f"{park_base_url}&api_key={np_api_key}"
    response_json = requests.get(park_url).json()
    parks_data = response_json['data']

    for i in parks_data:
        parks.insert_one(i)
        print("Data Inserted")
