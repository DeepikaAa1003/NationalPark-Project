from pymongo import MongoClient
from config import connect_string

class NPS_Mongo():

    def __init__(self):
        self.client = MongoClient(connect_string)
        self.db = self.client.NationalParksDB
        self.parks = self.db.parks
        self.activities = self.db.Activities

    # Initialize PyMongo to work with MongoDBs
    # client = MongoClient(connect_string)

    # # Define database and collection
    # db = client.NationalParksDB
    # parks_collection = db.parks
    # activities_collection = db.Activities

    def fetchParksByState(self, state):
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

    def fetchParksByActivity(self,activity):
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

    def fetchParksByParkName(self,parkname):
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

    def fetchParksBySTandAct(self,state, activity):
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


    def fetchParksByStAndPark(self,state,parkname):
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

    def fetchParksByActAndPark(self,activity,parkname):
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


    def fetchParksByActStateAndPark(self,activity, state, parkname):
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

    def fetchParksByParkCode(self,parkcode):
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

    def fetchAllParksNames(self):
        parks_names = []
        parksdata = self.parks.find({})
        for park in parksdata:
            parks_names += [(park["fullName"])]
        print(parks_names)
        print(len(parks_names))
        return parks_names

    def fetchAllStates(self):
        states_list = []
        parksdata = self.parks.find({})
        for park in parksdata:
            states_list+= [(park["states"])]
        print(states_list)
        print(len(states_list))
        return states_list

    def fetchAllActivities(self):
        activities_list = []
        activitiesdata = self.activities.find({})
        for activity in activitiesdata:
            activities_list += [activity["name"]]
        print(activities_list)
        print(len(activities_list))
        return activities_list