# Imports
import requests
import pymongo
import json

# Importing API key
from config import api_key

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.NationalParksDB
collection = db.activities

# Drops collection if available to remove duplicates
db.Activities.drop()

collection = db.Activities

## Get activity list from API
url = "https://developer.nps.gov/api/v1/"
with open('activity.json', 'w') as f:   
        activity_url= f"{url}activities?&api_key={api_key}"
        print(activity_url)
        # Retrieve page with the requests module
        response = requests.get(activity_url).json() 
        json.dump(response, f)

        activities = response["data"]
    
        for i in activities:
            collection.insert_one(i)
            print("Data Inserted")


## Populate thing to do
# Drops collection if available to remove duplicates
db.ThingsToDo.drop()
collection = db.ThingsToDo
counter = 0
while(counter <= 850):
    with open('thingstodo.json', 'w') as f:   
            thingstodoURL= f"{url}thingstodo?&api_key={api_key}&start={counter}"
            print(thingstodoURL)
            # Retrieve page with the requests module
            response = requests.get(thingstodoURL).json() 
            json.dump(response, f)

            thingstodo = response["data"]
        
            for i in thingstodo:
                collection.insert_one(i)
                print("Data Inserted")
                counter+=1
