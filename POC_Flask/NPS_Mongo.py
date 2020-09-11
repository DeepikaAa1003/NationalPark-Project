from pymongo import MongoClient
from config import connect_string

# Initialize PyMongo to work with MongoDBs
client = MongoClient(connect_string)

# Define database and collection
db = client.NationalParksDB

def fetchParksByState(state):
    parks = db.parks.find({
            "addresses": { "$elemMatch": {"stateCode":state } }
    })
    print("Inside fetchParksByState")
    results = []
    for park in parks:
        park.pop('_id') 
        results.append(park)
    print(results)
    return results

def fetchParksByActivity(activity):
    parks = db.parks.find({
           "activities": { "$elemMatch": {"name":activity } }
    })
    print("Inside fetchParksByActivity")
    results = []
    for park in parks:
        park.pop('_id') 
        results.append(park)
    print(results)
    
    return results

def fetchParksByParkName(parkname):
    parks = db.parks.find({
          "fullName":  parkname
    })
    print("Inside fetchParksByParkName")
    results = []
    for park in parks:
        park.pop('_id') 
        results.append(park)
    print(results)
    return results

def fetchParksBySTandAct(state, activity):
    parks = db.parks.find({"$and": [
    { "activities": { "$elemMatch": {"name":activity } } },
    { "addresses": { "$elemMatch": {"stateCode": state } } }]}

    )
    print("Inside fetchParksBySTandAct")
    # Return results
    results = []
    for park in parks:
        park.pop('_id') 
        results.append(park)
    print(results)
    return results


def fetchParksByStAndPark(state,parkname):
    parks = db.parks.find({"$and": [
    { "fullName":  parkname},
    { "addresses": { "$elemMatch": {"stateCode": state } } }]}

    )
    print("Inside fetchParksByStAndPark")
    results = []
    for park in parks:
        park.pop('_id') 
        results.append(park)
    print(results)
    return results

def fetchParksByActAndPark(activity,parkname):
    parks = db.parks.find({"$and": [
    { "fullName":  parkname},
    { "activities": { "$elemMatch": {"name":activity } } }]}

    )
    print("Inside fetchParksByActAndPark")
    results = []
    for park in parks:
        park.pop('_id') 
        results.append(park)
    print(results)
    return results


def fetchParksByActStateAndPark(activity, state, parkname):
    parks = db.parks.find({"$and": [
    { "fullName":  parkname},
    { "activities": { "$elemMatch": {"name":activity } } },
    { "addresses": { "$elemMatch": {"stateCode": state } } }]}

    )
    print("Inside fetchParksByActStateAndPark")
    results = []
    for park in parks:
        park.pop('_id') 
        results.append(park)
    print(results)
    return results

def fetchParksByParkCode(parkcode):
    parks = db.parks.find({
          "parkCode":  parkcode
    })
    print("Inside fetchParksByParkCode")
    results = []
    for park in parks:
        park.pop('_id') 
        results.append(park)
    print(results)
    return results

