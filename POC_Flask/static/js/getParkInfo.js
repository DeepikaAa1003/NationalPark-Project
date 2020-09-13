let parkcode = d3.select("#parkID").text()
console.log(parkcode)

function getParkInfo(parkcode){
    let parkDataURL = `/parks/v1.0/ParkDetailsbyParkCode/${parkcode}`;

    d3.json(parkDataURL).then((parkData) => {
        console.log(parkData);
        let park = parkData[0]
        
        // Park Page Header
        d3.select("#parkName").select("strong").text(park.fullName)

        // Pic Slideshow
        d3.selectAll(".picSlide").remove()
        park.images.forEach((img) => {
            d3.select("#parkPics").append("div").attr("class", "carousel-item picSlide")
                .append("img").attr("src", img.url).attr("class", "d-block w-100")
                console.log(img.url)
        })
        d3.select(".picSlide").attr("class", "carousel-item picSlide active")

        // About park Card
        d3.select("#aboutText").text(park.description)
        d3.select("#aboutURL").attr("href", park.url)
        d3.select("#wetherText").text(park.weatherInfo)

        // Park Entrance Fees Card
        park.entranceFees.forEach((entryOption) => { //TODO: loop through and list: "title, cost" (could add with description as tool tip when hovering over a line)
            let costUnformatted = parseFloat(entryOption.cost)
            let costFormatted = '$' + costUnformatted.toFixed(2).replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
            d3.select("#feeOptions").append("li").text(`${costFormatted} USD - ${entryOption.description}`)

        console.log(entryOption);

        });
       
        // Contact Info Card
        let phoneObj = park.contacts.phoneNumbers.filter( num => num.type === 'Voice')
            addressObj = park.addresses.filter( address => address.type === 'Mailing');

        d3.select("#phoneNum").html(`<strong>Phone Number:</strong><br>${phoneObj[0].phoneNumber}`)
        d3.select("#mailingAddr").html(`<strong>Mailing Address:</strong><br>${addressObj[0].line1}, ${addressObj[0].line2}, ${addressObj[0].city}, ${addressObj[0].stateCode}, ${addressObj[0].postalCode}`)
        d3.select("#email").html(`<strong>Email Address:</strong><br>${park.contacts.emailAddresses[0].emailAddress}`)
        d3.select("#directDet").html(`<strong>Directions to ${park.name}:</strong><br>${park.directionsInfo}`)
        d3.select("#diectURL").attr("href", park.directionsUrl)

        // Activities Card
        let activityList = "";
        park.activities.forEach((activity) => {
            activityList = activityList + ", " + activity.name;
            console.log(activity.name)
        })
        activityList = activityList.substring(2);
        d3.select("#activityList").text(activityList);

        //Operating Hours
        park.operatingHours.forEach((option)=> {
            d3.select("#opHrs").append("li").text(option.description)
        })
    })
}

getParkInfo(parkcode);