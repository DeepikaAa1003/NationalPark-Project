from pymongo import MongoClient
from config import connect_string
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Initialize PyMongo to work with MongoDBs
client = MongoClient(connect_string)
print(client)

# Define database and collection
db = client.NationalParksDB
parks_collection = db.parks
activities_collection = db.Activities
month_collection = db.monthly_visits_2019

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

def fetchAllParksNames():
    parks_names = []
    for park in parks_collection.find():
        parks_names += [park["fullName"]]
    print(parks_names)
    print(len(parks_names))
    return parks_names

def fetchAllStates():
    states_data = []
    for states in parks_collection.find():
        states_data += [states["states"]]
    states_list = list(set(states_data))
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

def fetchAllMonths():
    months_list = []
    query = month_collection.find_one()
    month_obj = query["month"]
    for j,k in month_obj.items():
        months_list.append(j)      
    print(months_list)
    return months_list

def fetchAllRegions():
    regions_data = []
    for region in month_collection.find():
        regions_data += [region["region"]]
    regions_list = list(set(regions_data))
    print(regions_list)
    print(len(regions_list))
    return regions_list

def fetchParkCodeByRegion(region_name):
    region_name = region_name + " "
    parks = month_collection.find({
           "region": region_name})
    park_codes_list = []
    for park in parks:
        print(park)
        park_codes_list.append(park["park_code"])
    print(park_codes_list)
    return park_codes_list

def fetchCoordinatesByCodeList(park_codes_list):
    park_by_region = []
    for code in park_codes_list:
        temp = db.parks.find({
            "parkCode": code
        })
        for i in temp:
            i.pop('_id')
            park_by_region.append(i)

    return(park_by_region)

fetchParkCodeByRegion("Southeast")








