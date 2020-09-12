
function buildmap(region_name){
    document.getElementById('regionmap').innerHTML = "<div id='map' style='width: 100%; height: 100%;'></div>";
    const url = `/parks/v1.0/ParksCodesByRegion/${region_name}`
    d3.json(url).then((parks) =>{
        console.log(parks);

        coordinates = [];

        parks.forEach(park => {

            coordinates.push([parseFloat(park.latitude),parseFloat(park.longitude)])

        })

        console.log(coordinates)

        const myMap = L.map("map", {
        center: [37.09, -95.71],
        zoom: 5
        });
  
         // Add a tile layer
        L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
        tileSize: 512,
        maxZoom: 18,
        zoomOffset: -1,
        id: "mapbox/streets-v11",
        accessToken: API_KEY
        }).addTo(myMap);


        coordinates.forEach(coord => {
            L.marker(coord)
            .addTo(myMap);
        })
        

    });

};

function optionChangedRegion(region){
    console.log(region);
    buildmap(region)
};


d3.json("/parks/v1.0/AllRegions/").then(initRegion => {
    console.log(initRegion[0])
    buildmap(initRegion[0]);
});

