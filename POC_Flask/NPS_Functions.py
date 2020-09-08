import requests
import pymongo
import json

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.NationalParksDB

def findonePark():
    oneParkDict = db.parks.find({ "activities": { "$elemMatch": {"name":"Birdwatching" } } })
    print("Inside findonePark")

    return oneParkDict

def findParksByState():
   
    parks = db.parks.find({"$and": [
    { "activities": { "$elemMatch": {"name":"Birdwatching" } } }
    ,{ "addresses": { "$elemMatch": {"stateCode":"UT" } } }]}

    )
    print("Inside findParksByState")
    # Return results
    return parks
