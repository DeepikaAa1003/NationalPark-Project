from pymongo import MongoClient
from config import connect_string

class NPS_Mongo():

    def __init__(self):
        self.client = MongoClient(connect_string)
        self.db = self.client.NationalParksDB
        self.parks = self.db.parks
        self.activities = self.db.Activities
        self.month_collection = self.db.monthly_visits_2019
        self.last_decade = self.db.last_decade_visits

    

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
        parks_names.sort()
        print(parks_names)
        print(len(parks_names))
        return parks_names

    def fetchAllStates(self):
        states_list = []
        parksdata = self.parks.find({})
        for park in parksdata:
            templist = park["states"].split(",")
            for i in templist:
                if(i not in states_list):
                     states_list+= [i]
        states_list.sort()
        print(states_list)
        print(len(states_list))
        return states_list

    def fetchAllActivities(self):
        activities_list = []
        activitiesdata = self.activities.find({})
        for activity in activitiesdata:
            activities_list += [activity["name"]]
        activities_list.sort()
        print(activities_list)
        print(len(activities_list))
        return activities_list

    def fetchAllMonths(self):
        months_list = []
        query = self.month_collection.find_one()
        month_obj = query["month"]
        for j,k in month_obj.items():
            months_list.append(j) 
         
        print(months_list)
        return months_list

    def fetchAllRegions(self):
        regions_data = []
        for region in self.month_collection.find():
            regions_data += [region["region"]]
        regions_list = list(set(regions_data))
        print(regions_list)
        print(len(regions_list))
        return regions_list
    
    def fetchAvailableVisitsParksNames(self):
        parks_names = []
        for park in self.month_collection.find():
            parks_names += [park["park_name"]]
        print(parks_names)
        print(len(parks_names))
        return parks_names

    def fetchParkCodeByRegion(self,region_name):
        region_name = region_name + " "
        parks = self.month_collection.find({
            "region": region_name})
        park_codes_list = []
        for park in parks:
            print(park)
            park_codes_list.append(park["park_code"])
        print(park_codes_list)
        return park_codes_list

    def fetchCoordinatesByCodeList(self,park_codes_list):
        park_by_region = []
        for code in park_codes_list:
            temp = self.parks.find({
                "parkCode": code
            })
            for i in temp:
                i.pop('_id')
                park_by_region.append(i)

        return(park_by_region)

    def fetchVisits2019ByRegion(self,selected_region):
        if selected_region == "Alaska":
            selected_region = selected_region
        else:
            selected_region = selected_region + " " 
        park_data = self.last_decade.find({"region": selected_region})
        parks_visits = []
        for park in park_data:
            park.pop('_id') 
            parks_visits.append(park)
        print(len(parks_visits))
        return parks_visits

    def fetchMonthlyVisitsByPark(self,park):
        park_data = self.month_collection.find({"park_name":park})
        parks_monthly_visits = []
        for park in park_data:
            park.pop('_id')
            parks_monthly_visits.append(park)
            print(parks_monthly_visits)
            return parks_monthly_visits

    def fetchMonthlyVisitsByRegion(self,region_input):
        if region_input == "Alaska":
            region_input = region_input
        else:
            region_input = region_input + " " 
        park_montly_data = self.month_collection.find({"region": region_input})
        parks_monthly_visits = []
        for park in park_montly_data:
            park.pop('_id') 
            parks_monthly_visits.append(park)
        print(len(parks_monthly_visits))
        return parks_monthly_visits

