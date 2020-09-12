let selectedParkName = "", selectedState = "", selectedActivity = "";
let searchParksButton = d3.select("#park");
// selectedParkName = d3.select("#selParkName").value;
// selectedActivity = d3.select("#selActivity").value;
// selectedState = d3.select("#selStates").value;
// selectedState = "";
// selectedParkName = "";
// selectedActivity = "";
let searchCriteria = "";
let tbody = d3.select("#searchResults");

function statechanged(state) {
    // Fetch new data each time a new sample is selected
    selectedState = state;
  
}
function activitychanged(activity) {
// Fetch new data each time a new sample is selected
selectedState = activity;

}
function parkchanged(parkname) {
// Fetch new data each time a new sample is selected
selectedState = parkname;

}
function searchParks(event){


    
    // console.log("Searching Parks");
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
    ExtractData(searchCriteria, searchParametersList);

}
  
function ExtractData(searchCriteria, searchParametersList){
    // console.log("inside extractdata");
    let dataUrl = `/parks/v1.0/${searchCriteria}`;


    searchParametersList.forEach(search => {
        dataUrl = `${dataUrl}/${search}`;
    });
    console.log(dataUrl);
       
    d3.json(dataUrl).then((data) => {
        // console.log(data);
        data.forEach((park) => {
             console.log(park);
            var row = tbody.append("tr");
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
                
                
        });
    });
       
    
}
  // Use D3 `.on` to attach a click handler for the upvote
  searchParksButton.on("click", searchParks);
  