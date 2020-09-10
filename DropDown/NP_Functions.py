import pymongo
from config import credentials
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Initialize PyMongo to work with MongoDBs
client = pymongo.MongoClient('mongodb://localhost:27017')

# Define database and collection
db = client.NationalParksDB
parks_collection = db.parks
activities_collection = db.Activities

def fetchAllParksNames():
    parks_names = []
    for park in parks_collection.find():
        parks_names += [park["fullName"]]
    print(parks_names)
    print(len(parks_names))
    return parks_names

def fetchAllStates():
    states_list = []
    for states in parks_collection.find():
        states_list += [states["states"]]
    print(states_list)
    print(len(states_list))
    return states_list

def fetchAllActivities():
    activities_list = []
    for activity in activities_collection.find():
        activities_list += [activity["name"]]
    print(activities_list)
    print(len(activities_list))
    return activities_list
