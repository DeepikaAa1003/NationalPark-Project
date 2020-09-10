from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import NPS_Mongo

# Create an instance of Flask
app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
#    Extract list of states, activities and park names to display in drop down values

    # Return template and data
    return render_template("index.html")


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

# Get all activities

# Get all states

# Get all park names

# Get Camground data by Park Code

# Get ThingsToDO by Park Code

# Get Last Decade visits by park code( to get last decade visits for a particular park)

# Get Last Decade visits by Year ( To get visits for all parks for a particular year)

# Get monthly visits by Month ( Pass a particular month like Jan and get visits of all parks)



if __name__ == "__main__":
    app.run(debug=True)
