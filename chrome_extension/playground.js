// get date and time of event in string format from StubHub HTML
// will need to format it in a way that would best be represented in the database
document.getElementsByClassName("sc-kzXxXt hXIoxu")[0].children[0].innerText

// will return an array w/ date time info w/o the '•' char
// currently has the form of ['Month (abbrev) day', 'weekday (abbrev)', 'time(am/pm)', 'year']
document.getElementsByClassName("sc-kzXxXt hXIoxu")[0].children[0].innerText.split(' • ')

// get the URL needed for the POST request later to get tickets info
document.baseURI