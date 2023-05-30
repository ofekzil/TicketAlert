// USE THIS METHOD
// using HTML is unreliable (chnages often), so instead use baseURI to get performer and city, and date of form 12 24 2022
let url = document.baseURI.split('?')[0]
let info = url.split('/')[3].split('-') // always at index 3 as indices 0,1,2 have values [https,'', www.stubhub.ca] no matter the event

// check if str begins with a lowercase english char
function capitalizeFirst(str) {
    let pattern = /[a-z].*/
    return pattern.test(str) ? str.charAt(0).toUpperCase() + str.slice(1) : str;
}

// capitalize first char of every non-numeric string
info = info.map(capitalizeFirst)

let i = 0
let performer = ""
let date = ""
while (i < info.length) {
    if (info[i] === 'Tickets') {
        i++;
        break;
    }
    performer += info[i] + " "
    i++
}

while (i < info.length) {
    date += info[i] + " "
    i++
}

performer = performer.substring(0, performer.length - 1)
date = date.substring(0, date.length - 1) // date is of format

// function to validate url using regex, check it's a proper stubhub event page
function validateUrl(url) {
    let pattern = /https:\/\/www\.stubhub(\.[a-z]+)+\/([a-z]+\-)+tickets\-(\d{1,2}-){2}\d{4}\/event\/\d+\//
    return pattern.test(url)
}

// get the coordinates of the user. 
// Stored in lng and lat. Might turn into globals or return them.
// Currently requires user permission from tab, but can be avoided if permissions are given in Chrome extension
function getCoords() {
    let lng, lat;
    navigator.geolocation.getCurrentPosition(
        // Success callback function
        (position) => {
            // Get the user's latitude and longitude coordinates
            lat = position.coords.latitude;
            lng = position.coords.longitude;
            
            // Do something with the location data, send it to the JSON to be sent to Lambda
            console.log(`latitude: ${lat}, longitude: ${lng}`);
        },

        // Error callback function
        (error) => {
            // Handle errors, e.g. user denied location sharing permissions
            console.error("Error getting user location:", error);
        }
    );
}

// gets a list of currency codes
Intl.supportedValuesOf("currency")

// to send api call to invoke lambda w/ data to insert
// likely works, can also maybe use fetch
var request = new XMLHttpRequest();
request.open("POST", apiGatewayUrl)
request.send({"operation" : "insert", "info" : 
            {"performerAndCity" : "performer and city", "eventDate" : " 8 9 2024", "eventUrl" : "https://www.stubhub.com",
        "threshold" : 30, "email" : "myEmail@gmail.com"}})

// api call w/ fetch (works from extension console)

function postFetch(url, sendData) {

    fetch(url, {
            method: 'POST',
            body: JSON.stringify(sendData),
            })
            .then((res) => res.json())
            .then((json) => {
                console.log(json);
                });
    }

postFetch("https://msyrsthbu1.execute-api.us-west-1.amazonaws.com/test/savedata", 
            {operation : "insert", "info" : 
            {"performerAndCity" : "performer and city", "eventDate" : " 8 9 2024", "eventUrl" : "https://www.stubhub.com",
             "threshold" : 30, "email" : "myEmail@gmail.com"}})

// DON'T USE THIS!!! HTML UNRELIABLE, CHNAGES OFTEN!!!
 
// get date and time of event in string format from StubHub HTML
// will need to format it in a way that would best be represented in the database
// OLD
document.getElementsByClassName("sc-kzXxXt hXIoxu")[0].children[0].innerText

// will return an array w/ date time info w/o the '•' char
// currently has the form of ['Month (abbrev) day', 'weekday (abbrev)', 'time(am/pm)', 'year']
// OLD
document.getElementsByClassName("sc-kzXxXt hXIoxu")[0].children[0].innerText.split(' • ')

// NEW
document.getElementsByClassName("sc-uSNQh eAYaOS")[0].children[0].innerText.split(' • ')

// get the URL needed for the POST request later to get tickets info
document.baseURI.split('?')[0]

// get artist name/teams playing (i.e. event name)
// OLD
document.getElementsByClassName("sc-dIvrsQ biCrYn sc-gefSNk kanhIe")[0].innerText

// NEW
document.getElementsByClassName("sc-bkbkJK hQibzx sc-jHUuBy fbSMOw")[0].innerText

// get info for venue and city in form of "Venue, City, Province/State, Country"
// OLD
document.getElementsByClassName("sc-jxLJeF dyWfWP")[0].innerText

// NEW
document.getElementsByClassName("sc-jfcRMW fKXaYH")[0].innerText


