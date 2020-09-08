from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import NPS_Functions

# Create an instance of Flask
app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    Parks_data = NPS_Functions.findonePark()
    # Return template and data
    return render_template("index.html", list=Parks_data)


# Route that will trigger the scrape function
@app.route("/SearchParks")
def scrape():

    
    Parks_data = NPS_Functions.findParksByState()
    print(Parks_data)
    return render_template("bonus.html", list=Parks_data)


if __name__ == "__main__":
    app.run(debug=True)
