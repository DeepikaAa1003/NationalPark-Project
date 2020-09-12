const myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 3.5
    });


function buildmap(region_name){
    
    const url = `/parks/v1.0/ParksCodesByRegion/${region_name}`
    console.log(url);
    d3.json(url).then((parks) =>{
        console.log(parks);

        const coordinates = [];
        const names = [];
        

        parks.forEach(park => {

            coordinates.push([parseFloat(park.latitude),parseFloat(park.longitude)])
            names.push(park.name)

        })
        console.log(coordinates)
        console.log(names);

      // Add a tile layer
      L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
      attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
      tileSize: 512,
      maxZoom: 18,
      zoomOffset: -1,
      id: "mapbox/streets-v11",
      accessToken: API_KEY
      }).addTo(myMap);
        
       coordinates.forEach((coord,i) => {
           console.log(names[i]);

       markers.push((L.marker(coord)).bindPopup("<p>" + names[i] + "</p>").addTo(myMap)
    
        )});

        console.log(markers);

    });

};

let markers = [];
function optionChangedRegion(region){
    console.log(markers);
    myMap.removeLayer(markers);
    console.log(markers);
    buildmap(region)
};


function init(){
  d3.json("/parks/v1.0/AllRegions/").then(initRegion => {
    console.log(initRegion[0])
    buildmap(initRegion[0]);
});

};

init()

//////////////Number of visits per park in a region for 2019/////////////




