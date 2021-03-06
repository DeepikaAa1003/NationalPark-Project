from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from NPS_Mongo import NPS_Mongo


#################################################
# Database Setup
#################################################
data = NPS_Mongo()

# Create an instance of Flask
app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/parks/v1.0/")
@app.route("/")
def home():

    # Find one record of data from the mongo database
#    Extract list of states, activities and park names to display in drop down values

    # Return template and data
    states = data.fetchAllStates()
    p_names = data.fetchAllParksNames()
    activity = data.fetchAllActivities()
    return render_template("index.html", states_list = states, parks_list = p_names, activities_list = activity)


# search park by state
@app.route("/parks/v1.0/SearchParksByState/<state>")
def fetchParksByState(state):
    return jsonify(data.fetchParksByState(state))

# search park by activity
@app.route("/parks/v1.0/SearchParksByActivity/<activity>")
def fetchParksByActivity(activity):
    return jsonify(data.fetchParksByActivity(activity))

# search park by Park Name
@app.route("/parks/v1.0/SearchParksByParkName/<parkname>")
def fetchParksByParkName(parkname):
    return jsonify(data.fetchParksByParkName(parkname))

# search park by state and activity
@app.route("/parks/v1.0/SearchParksByStAndAct/<state>/<activity>")
def fetchParksBySTandAct(state, activity):
    return jsonify(data.fetchParksBySTandAct(state, activity))

# search park by state and park name
@app.route("/parks/v1.0/SearchParksByStAndPark/<state>/<parkname>")
def fetchParksByStAndPark(state,parkname):
    return jsonify(data.fetchParksByStAndPark(state,parkname))


# search park by activity and park name
@app.route("/parks/v1.0/SearchParksByActAndPark/<activity>/<parkname>")
def fetchParksByActAndPark(activity,parkname):
    return jsonify(data.fetchParksByActAndPark(activity,parkname))

# search park by activity, state  and park name
@app.route("/parks/v1.0/SearchParksByActStateAndPark/<activity>/<state>/<parkname>")
def fetchParksByActStateAndPark(state,activity,parkname):
    return jsonify(data.fetchParksByActStateAndPark(state, activity, parkname))



# Get all park names

@app.route("/parksNames")
def parksNames():
    parks_data = data.fetchAllParksNames()
    return jsonify(parks_data)

# Get all states

@app.route("/states")
def states():
    states_data = data.fetchAllStates()
    return jsonify(states_data)

# Get All activities

@app.route("/activities")
def activities():
    activities_data = data.fetchAllActivities()
    return jsonify(activities_data)

#Load Park Details Page
@app.route("/parks/v1.0/ParkDetails/<parkcode>")
def fetchParksbyCode(parkcode):
    return render_template("park_details.html", parkcode = parkcode)


@app.route("/parks/v1.0/ParkDetailsbyParkCode/<parkcode>")
def fetchParksByParkCode(parkcode):
    return jsonify(data.fetchParksByParkCode(parkcode))


@app.route("/parks/v1.0/AvailableVisitsParknames/")
def fetchAvailableVisitsParksNames():
    return jsonify(data.fetchAvailableVisitsParksNames())
#Load Park Analysis Page
@app.route("/parks/v1.0/ParkAnalysis/")
def DisplayParkAnalysis():
    # Call function to extract list of park names
    parks_names = data.fetchAvailableVisitsParksNames()
    # Call function to extract list of months
    months = data.fetchAllMonths()
    # Call function to extract list of regions
    regions = data.fetchAllRegions()
    return render_template("park_analysis.html", parks_list = parks_names, months_list = months, regions_list = regions )

@app.route("/parks/v1.0/ParksCodesByRegion/<region>")
def fetchParksCodesByRegion(region):
    code_list = data.fetchParkCodeByRegion(region)
    parks_filtered = data.fetchCoordinatesByCodeList(code_list)
    return jsonify(parks_filtered)

@app.route("/parks/v1.0/AllRegions/")
def fetchAllRegions():

    return jsonify(data.fetchAllRegions())

@app.route("/parks/v1.0/Visits2019ByRegion/<region_name>")
def fetch2019VisitsByParkRegion(region_name):
    parks_visitors = data.fetchVisits2019ByRegion(region_name)
    return jsonify(parks_visitors)

@app.route("/parks/v1.0/MonthlyVisitsByPark/<park_name>")
def fetchMonthlyVisitsByParkName(park_name):
    park_monthly_visitors = data.fetchMonthlyVisitsByPark(park_name)
    return jsonify(park_monthly_visitors)

@app.route("/parks/v1.0/MonthlyVisitsByRegion/<input_region>")
def fetchMonthlyVisitsByParkRegion(input_region):
    parks_montly_visitors = data.fetchMonthlyVisitsByRegion(input_region)
    return jsonify(parks_montly_visitors)
# Get Camground data by Park Code

# Get ThingsToDO by Park Code

# Get Last Decade visits by park code( to get last decade visits for a particular park)

# Get Last Decade visits by Year ( To get visits for all parks for a particular year)

# Get monthly visits by Month ( Pass a particular month like Jan and get visits of all parks)



if __name__ == "__main__":
    app.run(debug=True)
