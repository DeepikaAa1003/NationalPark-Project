// const myMap = L.map("map", {
//     center: [37.09, -95.71],
//     zoom: 5
//     });

// function buildmap(region_name){
//     // document.getElementById('regionmap').innerHTML = "<div id='map' style='width: 100%; height: 100%;'></div>";
//     const url = `/parks/v1.0/ParksCodesByRegion/${region_name}`
//     console.log(url);
//     d3.json(url).then((parks) =>{
//         console.log(parks);

//         coordinates = [];

//         parks.forEach(park => {

//             coordinates.push([parseFloat(park.latitude),parseFloat(park.longitude)])

//         })

//         console.log(coordinates)

//         // const myMap = L.map("regionmap", {
//         // center: [37.09, -95.71],
//         // zoom: 5
//         // });
  
//          // Add a tile layer
//         L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//         attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//         tileSize: 512,
//         maxZoom: 18,
//         zoomOffset: -1,
//         id: "mapbox/streets-v11",
//         accessToken: API_KEY
//         }).addTo(myMap);


//         // points = []
//         // for (i=0; i<points.length; i++){
//         //     myMap.removeLayer(points[i])
//         // }
    
//         coordinates.map(coord => {
//             L.marker(coord)
//             .addTo(myMap);
//         })
//         // points.push(markers);


//     });

// };

// function optionChangedRegion(region){
//     console.log(region);
//     buildmap(region)
// };


// d3.json("/parks/v1.0/AllRegions/").then(initRegion => {
//     console.log(initRegion[0])
//     buildmap(initRegion[0]);
// });

// Create a map object
const myMap = L.map("map", {
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
  
  // Define a markerSize function that will give each city a different radius based on its population
  function markerSize(population) {
    return population / 40;
  }
  
  // Each city object contains the city's name, location and population
  const cities = [
    {
      name: "New York",
      location: [40.7128, -74.0059],
      population: 8550405
    },
    {
      name: "Chicago",
      location: [41.8781, -87.6298],
      population: 2720546
    },
    {
      name: "Houston",
      location: [29.7604, -95.3698],
      population: 2296224
    },
    {
      name: "Los Angeles",
      location: [34.0522, -118.2437],
      population: 3971883
    },
    {
      name: "Omaha",
      location: [41.2524, -95.9980],
      population: 446599
    }
  ];
  
  // Loop through the cities array and create one marker for each city object
  // cities.forEach(city => {
  //   console.log(city)
  //   L.circle(city.location, {
  //     fillOpacity: 0.75,
  //     color: "white",
  //     fillColor: "purple",
  //     // Setting our circle's radius equal to the output of our markerSize function
  //     // This will make our marker's size proportionate to its population
  //     radius: markerSize(city.population)
  //   }).bindPopup("<h1>" + city.name + "</h1> <hr> <h3>Population: " + city.population + "</h3>").addTo(myMap);
  // });
  
