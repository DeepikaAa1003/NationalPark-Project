from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import NPS_Mongo

# Create an instance of Flask
app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/parks/v1.0/")
@app.route("/")
def home():

    # Find one record of data from the mongo database
#    Extract list of states, activities and park names to display in drop down values

    # Return template and data
    states = NPS_Mongo.fetchAllStates()
    p_names = NPS_Mongo.fetchAllParksNames()
    activity = NPS_Mongo.fetchAllActivities()
    return render_template("index.html", states_list = states, parks_list = p_names, activities_list = activity)


# search park by state
@app.route("/parks/v1.0/SearchParksByState/<state>")
def fetchParksByState(state):
    return jsonify(NPS_Mongo.fetchParksByState(state))

# search park by activity
@app.route("/parks/v1.0/SearchParksByActivity/<activity>")
def fetchParksByActivity(activity):
    return jsonify(NPS_Mongo.fetchParksByActivity(activity))

# search park by Park Name
@app.route("/parks/v1.0/SearchParksByParkName/<parkname>")
def fetchParksByParkName(parkname):
    return jsonify(NPS_Mongo.fetchParksByParkName(parkname))

# search park by state and activity
@app.route("/parks/v1.0/SearchParksByStAndAct/<state>/<activity>")
def fetchParksBySTandAct(state, activity):
    return jsonify(NPS_Mongo.fetchParksBySTandAct(state, activity))

# search park by state and park name
@app.route("/parks/v1.0/SearchParksByStAndPark/<state>/<parkname>")
def fetchParksByStAndPark(state,parkname):
    return jsonify(NPS_Mongo.fetchParksByStAndPark(state,parkname))


# search park by activity and park name
@app.route("/parks/v1.0/SearchParksByActAndPark/<activity>/<parkname>")
def fetchParksByActAndPark(activity,parkname):
    return jsonify(NPS_Mongo.fetchParksByActAndPark(activity,parkname))

# search park by activity, state  and park name
@app.route("/parks/v1.0/SearchParksByActStateAndPark/<activity>/<state>/<parkname>")
def fetchParksByActStateAndPark(state,activity,parkname):
    return jsonify(NPS_Mongo.fetchParksByActStateAndPark(state, activity, parkname))



# Get all park names

@app.route("/parksNames")
def parksNames():
    parks_data = NPS_Mongo.fetchAllParksNames()
    return jsonify(parks_data)

# Get all states

@app.route("/states")
def states():
    states_data = NPS_Mongo.fetchAllStates()
    return jsonify(states_data)

# Get All activities

@app.route("/activities")
def activities():
    activities_data = NPS_Mongo.fetchAllActivities()
    return jsonify(activities_data)

#Load Park Details Page
@app.route("/parks/v1.0/ParkDetails/<parkcode>")
def fetchParksbyCode(parkcode):
    return render_template("park_details.html", parkcode = parkcode)


@app.route("/parks/v1.0/ParkDetailsbyParkCode/<parkcode>")
def fetchParksByParkCode(parkcode):
    return jsonify(NPS_Mongo.fetchParksByParkCode(parkcode))

#Load Park Analysis Page
@app.route("/parks/v1.0/ParkAnalysis/")
def DisplayParkAnalysis():
    # Call function to extract list of park names
    parks_names = NPS_Mongo.fetchAllParksNames()
    # Call function to extract list of months
    months = NPS_Mongo.fetchAllMonths()
    # Call function to extract list of regions
    regions = NPS_Mongo.fetchAllRegions()
    return render_template("park_analysis.html", parks_list = parks_names, months_list = months, regions_list = regions )

@app.route("/parks/v1.0/ParksCodesByRegion/<region>")
def fetchParksCodesByRegion(region):
    code_list = NPS_Mongo.fetchParkCodeByRegion(region)
    parks_filered = NPS_Mongo.fetchCoordinatesByCodeList(code_list)
    return jsonify(parks_filered)

@app.route("/parks/v1.0/AllRegions/")
def fetchAllRegions():

    return jsonify(NPS_Mongo.fetchAllRegions())

@app.route("/parks/v1.0/Visits2019ByRegion/<region>")
def fetch2019VisitsByParkRegion():
    return(NPS_Mongo.fetchVisits2019ByRegion())
# Get Last Decade visits by park code( to get last decade visits for a particular park)

# Get Last Decade visits by Year ( To get visits for all parks for a particular year)

# Get monthly visits by Month ( Pass a particular month like Jan and get visits of all parks)



if __name__ == "__main__":
    app.run(debug=True)
