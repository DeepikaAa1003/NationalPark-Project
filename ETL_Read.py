# Imports
import requests
import pymongo
import json

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.NationalParksDB

## Search park by activity and state

parks = db.parks.find({"$and": [
   { "activities": { "$elemMatch": {"name":"Birdwatching" } } }
   ,{ "addresses": { "$elemMatch": {"stateCode":"UT" } } }]}

)

## For park related data 

for park in parks:
    print("ParkName===" + park["fullName"])
    print("Lat and Long ===" + park["latLong"])
    print("Park code ====" + park["parkCode"])
    print("Park description ===" + park["description"])
    print("Pakr URL ===" + park["url"])
    emailList = park["contacts"]["emailAddresses"]
    for email in emailList:
        print("Email ==" + email["emailAddress"])
    acitivityList = park["activities"]
    for activity in acitivityList:
        print("activity Name ====" + activity["name"])
    imageList = park["images"]
    for image in imageList:
        print("Image URL=====" + image["url"])


## Find ThingsTodo for each park

Thingstodo = db.ThingsToDo.find(
    { "relatedParks": { "$elemMatch": {"parkCode": "frsp" } } }
)

for things in Thingstodo:
    print("things=====")
    print(things["title"])