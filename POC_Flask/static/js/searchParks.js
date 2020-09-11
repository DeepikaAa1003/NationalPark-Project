let selectedParkName = "", selectedState = "", selectedActivity = "";
let searchParksButton = d3.select("#park");
// var selectedParkName = d3.select("#selParkName");
// var selectedActivity = d3.select("#selActivity");
// var selectedStates = d3.select("#selStates");
selectedState = "TX";
selectedParkName = "";
selectedActivity = "";
let searchCriteria = "";
let tbody = d3.select("#searchResults");

function searchParks(event){

    // console.log("Searching Parks");
    let searchCriteria;
    // console.log(selectedState);
    // console.log(selectedActivity);
    // console.log(selectedParkName);

    if(selectedParkName == "" && selectedState == "" && selectedActivity == ""){
        alert("Please select a value to search the parks");
        
    }
    else if (selectedParkName != "" && selectedActivity != "" && selectedState != ""){
        searchCriteria = "SearchParksByActStateAndPark";
    }
    else if (selectedParkName != ""){
        if(selectedState != ""){
                searchCriteria = "SearchParksByStAndPark";
        }else{
            if(selectedActivity != ""){
                searchCriteria = "SearchParksByActAndPark";
            }else{
                searchCriteria = "SearchParksByParkName";
            }
        }
        
    } else if(selectedActivity != ""){
            if(selectedState != ""){
                searchCriteria = "SearchParksByStAndAct";
            }else{
                searchCriteria = "SearchParksByActivity";
            }
    }else{
        searchCriteria = "SearchParksByState";
        ExtractData(searchCriteria);
    }
    console.log(searchCriteria);

}
  
function ExtractData(searchCriteria){
    // console.log("inside extractdata");
    let dataUrl = `/parks/v1.0/${searchCriteria}`;


    if (searchCriteria == "SearchParksByState"){
        dataUrl = `${dataUrl}/${selectedState}`;

    }
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
  