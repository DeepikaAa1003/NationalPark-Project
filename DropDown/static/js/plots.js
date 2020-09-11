// function dropDwn(){

//   // ParkNames
//   d3.json("/parksNames").then((parks) => {
//     // console.log(parks)
//      //html dropDown selector
//     const nameSelect = d3.select("#selParkName");

//       //append "option" and value for each subject
//     parks.forEach(name =>{
//       const optionName = nameSelect.append("option");
//       optionName.text(name).property("value",name);
//     })
//   });

//   //Sates
//   d3.json("/states").then((states) => {
//     // console.log(states)
//      //html dropDown selector
//     const stateSelect = d3.select("#selStates");

//       //append "option" and value for each subject
//     states.forEach(park =>{
//       const optionState = stateSelect.append("option");
//       optionState.text(park).property("value",park);
//     })
//   });

//   //Activities
//   d3.json("/activities").then((activities) => {
//     console.log(activities)
//      //html dropDown selector
//     const activitySelect = d3.select("#selActivity");

//       //append "option" and value for each subject
//     activities.forEach(activity =>{
//       const optionActivity = activitySelect.append("option");
//       optionActivity.text(activity).property("value",activity);
//     })
//   });

// };

// dropDwn()