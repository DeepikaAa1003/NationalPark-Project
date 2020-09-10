let selectedParkName = "", selectedState = "", selectedActivity = "";
let searchParksButton = d3.select("#park");
// var selectedParkName = d3.select("#selParkName");
// var selectedActivity = d3.select("#selActivity");
// var selectedStates = d3.select("#selStates");
selectedState = "TX";
selectedParkName = "";
selectedActivity = "";
let searchCriteria = "";

function searchParks(event){

    console.log("Searching Parks");
    let searchCriteria;
    console.log(selectedState);
    console.log(selectedActivity);
    console.log(selectedParkName);

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
    }
    console.log(searchCriteria);
  };
  
  // Use D3 `.on` to attach a click handler for the upvote
  searchParksButton.on("click", searchParks);
  