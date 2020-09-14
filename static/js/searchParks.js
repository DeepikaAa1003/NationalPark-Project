let selectedParkName = "", selectedState = "", selectedActivity = "";
let searchParksButton = d3.select("#park");
let searchCriteria = "";
let parks = L.layerGroup();


 // Create a map object
const myMap = L.map("mapid", {
    center: [37.09, -95.71],
    zoom: 5
});

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        tileSize: 512,
        maxZoom: 18,
        zoomOffset: -1,
        id: "mapbox/streets-v11",
        accessToken: API_KEY
    }).addTo(myMap);

loadTop10Parks() ;

function statechanged(state) {
    // Fetch new data each time a new state is selected
    selectedState = state;
  
}
function activitychanged(activity) {
// Fetch new data each time a new activity is selected
    selectedActivity = activity;

}
function parkchanged(parkname) {
// Fetch new data each time a new parkname is selected
    selectedParkName = parkname;

}
function loadParkMap(parks){
   
    console.log("========================Inside map function");
    
    console.log(parks);
    // Loop through the cities array and create one marker for each city, bind a popup containing its name and population add it to the map
    parks.forEach(coord => {
        L.marker(coord)
        .addTo(myMap);
    })
    
    
  }

function searchParks(event){
    
    // Remove existing layers from map
    myMap.eachLayer(function (layer) {myMap.removeLayer(layer);});
    // Add a tile layer
    L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        tileSize: 512,
        maxZoom: 18,
        zoomOffset: -1,
        id: "mapbox/streets-v11",
        accessToken: API_KEY
    }).addTo(myMap);

    // Remove existing table rows
    let tabledata = d3.select("#searchParkResults");
    tabledata.remove();
    // Find out which drop down values are selected and decide the selection criteria
    let searchCriteria;
    let searchParametersList = [];
    console.log(selectedState);
    console.log(selectedActivity);
    console.log(selectedParkName);

    if(selectedParkName == "" && selectedState == "" && selectedActivity == ""){
        alert("Please select a value to search the parks");
        
    }
    else if (selectedParkName != "" && selectedActivity != "" && selectedState != ""){
        searchCriteria = "SearchParksByActStateAndPark";
        searchParametersList.push(selectedState);
        searchParametersList.push(selectedActivity);
        searchParametersList.push(selectedParkName);
    }
    else if (selectedParkName != ""){
        if(selectedState != ""){
                searchCriteria = "SearchParksByStAndPark";
                searchParametersList.push(selectedState);
                searchParametersList.push(selectedParkName);
        }else{
            if(selectedActivity != ""){
                searchCriteria = "SearchParksByActAndPark";
                searchParametersList.push(selectedActivity);
                searchParametersList.push(selectedParkName);
            }else{
                searchCriteria = "SearchParksByParkName";
                searchParametersList.push(selectedParkName);
            }
        }
        
    } else if(selectedActivity != ""){
            if(selectedState != ""){
                searchCriteria = "SearchParksByStAndAct";
                searchParametersList.push(selectedState);
                searchParametersList.push(selectedActivity);
            }else{
                searchCriteria = "SearchParksByActivity";
                searchParametersList.push(selectedActivity);
            }
    }else{
        searchCriteria = "SearchParksByState";
        searchParametersList.push(selectedState);
        
    }
    
    console.log(searchCriteria);
    console.log(searchParametersList);
    //Extract data from DB based on search criteria
    ExtractData(searchCriteria, searchParametersList);
   
    
}

function ExtractData(searchCriteria, searchParametersList){

    
    let divdata = d3.select("#searchparksdiv");
    // Create a new table
    const tableEnter = divdata.append('table')
      .attr('id', "searchParkResults")
      .attr('class', 'table table-striped table-sm table-dark');
    // Create table headers
    let tablehead = tableEnter.append("thead");
    let headrow = tablehead.append("tr")
            .attr('class', 'bg-info');
    
    let headcell = headrow.append("th");
    headcell.html("Park Name");
    headcell = headrow.append("th");
    headcell.html("Contact Details");
    headcell = headrow.append("th");
    headcell.html("Park Type");
    headcell = headrow.append("th");
    headcell.html("More Info");
    // Create a new table body
    tablebody = tableEnter.append("tbody");
    
    
    // Prepare the URL to get the data for selected criteria and parameters from Mongo DB
    let dataUrl = `/parks/v1.0/${searchCriteria}`;


    searchParametersList.forEach(search => {
        dataUrl = `${dataUrl}/${search}`;
    });
    console.log(dataUrl);
    
    d3.json(dataUrl).then((data) => {

    // Loop through parks data
        
        data.forEach((park) => {
            
            console.log(park);
            if(park.latitude != "" && park.longitude != ""){
                    // Create single marker and add to map
                    singleParkMarker = L.marker([parseFloat(park.latitude),parseFloat(park.longitude)])
                                        .bindPopup(`<h5><strong>${park["fullName"]}, ${park["states"]}</strong><h5>`)
                                        .addTo(myMap);
                    parks.addLayer(singleParkMarker);
                    
                    // Add rows and columns ot the table and fill in the data
                    var row = tablebody.append("tr");
                        var cell = row.append("td");
                        cell.html(park["fullName"]);
                        emailList = park["contacts"]["emailAddresses"]
                        emailInfo = "";
                        emailList.forEach(email=> {
                            emailInfo = `${emailInfo},${email['emailAddress']}`;
                        }); 
                        let emailInfo1 = emailInfo.slice(1);
                        var cell = row.append("td");
                        cell.html(emailInfo1);
                        var cell = row.append("td");
                        cell.html(park["designation"]);
                        var cell = row.append("td");
                        cell.html(`<a href="/parks/v1.0/ParkDetails/${park["parkCode"]}">More Info</a>`);
                
            }
        });
        
    });
    
    selectedState = "";
    selectedActivity = "";
    selectedParkName = "";
    
    
}
function loadTop10Parks() {
    //Due to shortage of time hardcoded the top 10 park names else we could have used beautiful soup to web scrap
    
    let top10ParksList = ["yose", "yell", "glac", "grca", "zion", "grte", "brca", "arch", "romo", "hale" ];
    let divdata = d3.select("#searchparksdiv");
    // Create a new table
    const tableEnter = divdata.append('table')
      .attr('id', "searchParkResults")
      .attr('class', 'table table-striped table-sm table-dark');
    // Create table headers
    let tablehead = tableEnter.append("thead");
    let headrow = tablehead.append("tr")
            .attr('class', 'bg-info');
    
    let headcell = headrow.append("th");
    headcell.html("Park Name");
    headcell = headrow.append("th");
    headcell.html("Contact Details");
    headcell = headrow.append("th");
    headcell.html("Park Type");
    headcell = headrow.append("th");
    headcell.html("More Info");
    // Create a new table body
    tablebody = tableEnter.append("tbody");
    
    
    top10ParksList.forEach(parkcode=> {
        let dataUrl = `/parks/v1.0/ParkDetailsbyParkCode/`;
        dataUrl = dataUrl + parkcode;
        d3.json(dataUrl).then((data) => {
            data.forEach((park) => {
            
                console.log(park);
                if(park.latitude != "" && park.longitude != ""){
                        // Create single marker and add to map
                        singleParkMarker = L.marker([parseFloat(park.latitude),parseFloat(park.longitude)])
                                            .bindPopup(`<h5>${park["fullName"]}, ${park["states"]}<h5>`)
                                            .addTo(myMap);
                        parks.addLayer(singleParkMarker);

                        var row = tablebody.append("tr");
                        var cell = row.append("td");
                        cell.html(park["fullName"]);
                        emailList = park["contacts"]["emailAddresses"]
                        emailInfo = "";
                        emailList.forEach(email=> {
                            emailInfo = `${emailInfo},${email['emailAddress']}`;
                        }); 
                        let emailInfo1 = emailInfo.slice(1);
                        var cell = row.append("td");
                        cell.html(emailInfo1);
                        var cell = row.append("td");
                        cell.html(park["designation"]);
                        var cell = row.append("td");
                        cell.html(`<a href="/parks/v1.0/ParkDetails/${park["parkCode"]}">More Info</a>`);
                }
            });
        });
    });
}

  // Use D3 `.on` to attach a click handler
  searchParksButton.on("click", searchParks);

  