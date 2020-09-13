

let parkcode = d3.select("#parkID").text()
console.log(parkcode)


function getParkInfo(parkcode){
    let parkDataURL = `/parks/v1.0/ParkDetailsbyParkCode/${parkcode}`;

    d3.json(parkDataURL).then((parkData) => {
        console.log(parkData);

        // About park
        var aboutParkDesc = parkData[0].description
            aboutParkWebsite = parkData[0].url;

        console.log(aboutParkDesc);
        console.log(aboutParkWebsite);

        // Park Entrance Fees
        parkData[0].entranceFees.forEach((entryOption) => { //TODO: loop through and list: "title, cost" (could add with description as tool tip when hovering over a line)
        
        console.log(entryOption);

        });
       
        // Contact Info
        var phoneObj = parkData[0].contacts.phoneNumbers.filter( num => num.type === 'Voice')
            contactPhone = phoneObj[0].phoneNumber
        
            contactEmail = parkData[0].contacts.emailAddresses[0].emailAddress; //Only takes first email (haven't seen a DB object with multiple EM's but list format suggests its possible)
            
            addressObj = parkData[0].addresses.filter( address => address.type === 'Mailing');
            contactAddress = `${addressObj[0].line1}, ${addressObj[0].line2}, ${addressObj[0].city}, ${addressObj[0].stateCode}, ${addressObj[0].postalCode}`

            directionsURL = parkData[0]

        console.log(contactPhone);
        console.log(contactAddress);
        console.log(contactEmail);

        // Activities

        parkData[0].activities.forEach((activity) => {
            let activitiesArr = []
            console.log(activity.name)
            //append activity to activitiesArr
        })
    })
}

getParkInfo(parkcode);

//a bunch of d3 slect stuff to get it into park_details.html