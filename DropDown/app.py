# dependencies
import NP_Functions
import pymongo
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Get all park names

@app.route("/parksNames")
def parksNames():
    parks_data = NP_Functions.fetchAllParksNames()
    return jsonify(parks_data)

# Get all states

@app.route("/states")
def states():
    states_data = NP_Functions.fetchAllStates()
    return jsonify(states_data)

# Get All activities

@app.route("/activities")
def activities():
    activities_data = NP_Functions.fetchAllActivities()
    return jsonify(activities_data)


if __name__ == "__main__":
    app.run(debug=True)



        