# US NATIONAL PARKS

Welcome to US National Parks interactive site. If you need a push to decided which park to visit, you are in the right place!

1. What is the purpose of this dashboard?

To present useful information, where any person can search key details about US Parks, leveraging our powerful filters, based on various parameters such as activities, states, park names; as well as demographic data visualization that will help potential visitors to take the best decision.

2. How this Dashboard is made of?

This a "FullStack" application based on three main layers:

- Database : Mongo Atlas
- Flask Python
- Front End

## Database

## Flask

## Front End

##### Used Tools : JavaScript, HTML/CSS, Bootstrap, D3, Leaflet Plotly.

Three views were generated leveraging the combination of the previous tools. HTML/CSS plus Bootstrap were the techniques used to build the structure/skeleton of each page.
With JavScript and D3 selection methods we were able to call data from our API enpoints, and to populate all dropdown lists, the "Main Parks Table, Images, Park Details & Info, etc.:

![NationalParks](Images/FirstView.PNG)

Leaflet and Plotly together with JS were used to build maps, bar charts, and line charts:

![NationalParks](Images/ThirdView.PNG)

3. How to run/use this application?

* You can use our web application through this link [National Parks Heroku](https://nationalparksdashboard.herokuapp.com/)
* You can also clone this repository in your local machine and run our application; but please keep in mind the following recommendations:
  - Be sure to have Pymongo installed.
  - Create a Local Mongo Database or a Cloud Mongo Altlas DB. You can populate this database....
  - Create a config.py file to store the DB connection as follow: connect_string = "mongodb+srv://DBUser:PASSWORD@cluster0.za3mz.mongodb.net/?retryWrites=true&w=majority". This will ensure the flask-DB channel.
  - For Leaflet you will need to generate a public token [MapBox](https://account.mapbox.com/access-tokens/) and store it within a config.js file inside the static/js folder.
* You can deploy this app to Heroku; or you can run it from localhost.

