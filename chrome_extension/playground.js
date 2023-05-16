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