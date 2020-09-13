//////////////Parks per Region/////////////
let region_select = "";
let month_select = "";
//Map Object by default
const myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 3.4
    });
//Initialize TileLayer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
    }).addTo(myMap);

//Park markers layerGroup
let markers = L.layerGroup()

//function that generates a map based on dropdown selected option
function buildmap(region_name){
    
    const url = `/parks/v1.0/ParksCodesByRegion/${region_name}`
    console.log(url);
    d3.select(".region").text(region_name)
    d3.json(url).then((parks) =>{
        console.log(parks);

        const coordinates = [];
        const names = [];
        
        //store coordinates and park names in arrays
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
        
        // create single makers and popup
        coordinates.forEach((coord,i) => {
        singleMarker = L.marker(coord).bindPopup("<p>" + names[i] + "</p>").addTo(myMap)
        //add every single marker to the grouplayer
        markers.addLayer(singleMarker)
        });

        console.log(markers);

    });

};


//////////////Number of visits per park in a region for 2019/////////////

//function that generates a bar plot based on selected region
function visits2019Plot(region_input){

    const visits_url = `/parks/v1.0/Visits2019ByRegion/${region_input}`
    console.log(visits_url);

    d3.json(visits_url).then((parks) =>{
        console.log(parks)

        const visits = {};
        const parksNames = {};

        //retrieve 2019 visits for every park of selected region
        parks.forEach((park,i) => {
            visits[park.park_code] = park.years["2019"]
            parksNames[park.park_name] = park.years["2019"]
            
        });

        console.log(visits);
        console.log(parksNames);

        //sort and slice visits
        const visitsArr = Object.entries(visits);
        const sortVisitsArr = visitsArr.sort(function(a, b) {
            return b[1] - a[1];
        });

        const parkNamesvisitsArr = Object.entries(parksNames);
        const byParkNameSortVisitsArr = parkNamesvisitsArr.sort(function(a, b) {
            return b[1] - a[1];
        });

        const sliceVisitsArr = sortVisitsArr.slice(0,20);
        const byParkNameSliceVisit = byParkNameSortVisitsArr.slice(0,20);

        console.log(sliceVisitsArr);
        console.log(byParkNameSliceVisit);

        const parksText = byParkNameSliceVisit.map(park => park[0]);
        console.log(parksText);

        const parksAxis = sliceVisitsArr.map(park => park[0]);
        console.log(parksAxis);

        const visitsAxis = sliceVisitsArr.map(park => park[1]);
        console.log(visitsAxis);

        //build plot
        const visitTrace = {
            x:parksAxis,
            y:visitsAxis,
            marker: {
                color: 'rgb(49,130,189)',
                opacity: 0.5
            },
            text: parksText,
            type: 'bar'
        };

        const visitsLayout = {
           
            xaxis: {tickfont: {
                size: 8},

                tickangle: -45,
                title: "Park Code"
            },
            yaxis: {tickfont: {
                    size: 8,
                    },
                title: "Visits 2019"
            },
            margin: {
                l: 100,
                r: 100,
                t: 40,
                b: 40,
            },

            title: `${region_input} Region`,

            paper_bgcolor: 'rgba(204,204,204)',
            plot_bgcolor: 'rgba(204,204,204)',
            width: 600,
            height: 300,
            showlegend: false,
        };

        const dataVisits = [visitTrace];

        Plotly.newPlot("chart1",dataVisits, visitsLayout);

    })

};

// event handler function based on selected region
function optionChangedRegion(region){

    console.log(markers);
    myMap.eachLayer(function (layer) {myMap.removeLayer(layer);});
    buildmap(region);
    visits2019Plot(region);
    region_select = region;
    monthlyVisitsRegionPark()
    

};


//////////////Monthly Visits Per Park/////////////

function monthlyVisits(park_input){

    const montlhyVisitsUrl = `/parks/v1.0/MonthlyVisitsByPark/${park_input}`
    console.log(montlhyVisitsUrl)

    d3.json(montlhyVisitsUrl).then(park =>{
    console.log(park);

    const months = park[0].month
    months_data = Object.entries(months)
    console.log(months_data);

      var monthNames = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
      };
      
      // sort the data array
    const sortedMonthVisits = months_data.sort(function(a, b) {
        // sort based on the value in the monthNames object
        return monthNames[a[0]] - monthNames[b[0]];
      });

    console.log(sortedMonthVisits);


    monthsAxis = sortedMonthVisits.map(month =>month[0]);
    console.log(monthsAxis)
    monthlyVisitsAxis = sortedMonthVisits.map(visit => visit[1]);
    console.log(monthlyVisitsAxis)
    const name_park = park[0].park_name;

     //build line plot
     const monthlyVisitsTrace = {
        x: monthsAxis,
        y: monthlyVisitsAxis,
        marker: {
            color: 'rgb(49,130,189)',
            opacity: 0.5
        },
        type: 'line'
    };

    const monthlyVisitsLayout = {
       
        xaxis: {tickfont: {
            size: 8},

            tickangle: -45,
            title: "Month"
        },
        yaxis: {tickfont: {
                size: 8,
                },
            title: "Visits"
        },
        margin: {
            l: 100,
            r: 100,
            t: 40,
            b: 40,
        },

        title: `${name_park} 2019 Visits`,

        paper_bgcolor: 'rgba(204,204,204)',
        plot_bgcolor: 'rgba(204,204,204)',
        width: 600,
        height: 300,
        showlegend: false,
    };

    const monthlyVisits = [monthlyVisitsTrace];

    Plotly.newPlot("chart2", monthlyVisits, monthlyVisitsLayout);
    
});

};

// event handler function based on selected park
function optionChangedPark(park){
    monthlyVisits(park)
};


//////////////For each park in a Region by Month/////////////

function monthlyVisitsRegionPark(){
     console.log(month_select);
     console.log(region_select);
     if (month_select != "" && region_select != ""){

    monthlyRegionUrl = `/parks/v1.0/MonthlyVisitsByRegion/${region_select}`
    d3.json(monthlyRegionUrl).then(parks =>{
        console.log(parks);

        const monthParkObj = {};
        const namesParksObj = {};
        parks.forEach(park =>{

            if (park in monthParkObj){
                monthParkObj[park.park_code].push(park.month[month_select])
            }
            else {
                monthParkObj[park.park_code] = park.month[month_select]
            };   

            if (park in namesParksObj){
                namesParksObj[park.park_name].push(park.month[month_select])
            }
            else {
                namesParksObj[park.park_name] = park.month[month_select]
            };
        })

        console.log(monthParkObj);
        console.log(namesParksObj);

        //sort and slice visits
        const byMonthVisitsArr = Object.entries(monthParkObj);
        const sortedByMonthVisitsArr = byMonthVisitsArr.sort(function(a, b) {
            return b[1] - a[1];
        });

        const byMonthParkNamesvisitsArr = Object.entries(namesParksObj);
        const byMonthParkNameSortVisitsArr = byMonthParkNamesvisitsArr.sort(function(a, b) {
            return b[1] - a[1];
        });

        const byMonthSliceVisitsArr = sortedByMonthVisitsArr.slice(0,20);
        const byMonthParkNameSliceVisit = byMonthParkNameSortVisitsArr.slice(0,20);

        console.log(byMonthSliceVisitsArr);
        console.log(byMonthParkNameSliceVisit);

        const parksTextArr = byMonthParkNameSliceVisit.map(park => park[0]);
        console.log(parksTextArr);

        const byMonthParksAxis = byMonthSliceVisitsArr.map(park => park[0]);
        console.log(byMonthParksAxis);

        const byMonthVisitsAxis = byMonthSliceVisitsArr.map(park => park[1]);
        console.log(byMonthVisitsAxis);

        //build plot
        const byMonthVisitTrace = {
            x:byMonthParksAxis,
            y:byMonthVisitsAxis,
            marker: {
                color: 'rgb(49,130,189)',
                opacity: 0.5
            },
            text: parksTextArr,
            type: 'bar'
        };

        const byMonthVisitsLayout = {
           
            xaxis: {tickfont: {
                size: 8},

                tickangle: -45,
                title: "Park Code"
            },
            yaxis: {tickfont: {
                    size: 8,
                    },
                title: `${month_select} Visits`
            },
            margin: {
                l: 100,
                r: 100,
                t: 40,
                b: 40,
            },

            title: `${region_select} Region`,

            paper_bgcolor: 'rgba(204,204,204)',
            plot_bgcolor: 'rgba(204,204,204)',
            width: 600,
            height: 300,
            showlegend: false,
        };

        const byMonthDataVisits = [byMonthVisitTrace];

        Plotly.newPlot("chart3",byMonthDataVisits, byMonthVisitsLayout);
        

    })
    }
};

// event handler function based on selected park
function optionChangedMonth(month_selected){
    month_select = month_selected;
    monthlyVisitsRegionPark();
};
