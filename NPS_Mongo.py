from pymongo import MongoClient
from config import connect_string

class NPS_Mongo():

    def __init__(self):
        self.client = MongoClient(connect_string)
        self.db = self.client.NationalParksDB
        self.parks = self.db.parksdata
        self.activities = self.db.Activities

    # Initialize PyMongo to work with MongoDBs
    # client = MongoClient(connect_string)

    # # Define database and collection
    # db = client.NationalParksDB
    # parks_collection = db.parks
    # activities_collection = db.Activities

    def fetchParksByState(state):
        parks = self.parks.find({
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
        parks = self.parks.find({
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
        parks = self.parks.find({
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
        parks = self.parks.find({"$and": [
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
        parks = self.parks.find({"$and": [
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
        parks = self.parks.find({"$and": [
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
        parks = self.parks.find({"$and": [
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
        parks = self.parks.find({
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
        parksdata = self.parks.find({})
        for park in parksdata:
            parks_names.append(park["fullName"])
        print(parks_names)
        print(len(parks_names))
        return parks_names

    def fetchAllStates():
        states_list = []
        parksdata = self.parks.find({})
        for park in parksdata:
            states_list.append(park["states"])
        print(states_list)
        print(len(states_list))
        return states_list

    def fetchAllActivities():
        activities_list = []
        activitiesdata = self.Activities.find({})
        for activity in activitiesdata:
            activities_list += [activity["name"]]
        print(activities_list)
        print(len(activities_list))
        return activities_list