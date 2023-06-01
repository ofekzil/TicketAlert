const API = "https://msyrsthbu1.execute-api.us-west-1.amazonaws.com/test/savedata";
const URL_PATTERN = /https:\/\/www\.stubhub(\.[a-z]+)+\/([a-z]+\-)+tickets\-(\d{1,2}-){2}\d{4}\/event\/\d+\//;
const EMAIL_PATTERN = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/;


// check if str matches regex pattern
function validate(str, pattern) {
    return pattern.test(str);
}

// check if str begins with a lowercase english char, and if so capitalize the first letter
function capitalizeFirst(str) {
    let pattern = /[a-z].*/;
    return pattern.test(str) ? str.charAt(0).toUpperCase() + str.slice(1) : str;
}

// set info to be sent to lambda, getting it from url and also including email and threshold
function setInfo(url, email, threshold) {
    let split = url.split('?')[0];
    let info = split.split('/')[3].split('-');
    info = info.map(capitalizeFirst);
    let i = 0;
    let performer = "";
    let date = "";
    while (i < info.length) {
        if (info[i] === 'Tickets') {
            i++;
            break;
        }
        performer += info[i] + " ";
        i++;
    }

    while (i < info.length) {
        date += info[i] + " ";
        i++;
    }

    performer = performer.substring(0, performer.length - 1);
    date = date.substring(0, date.length - 1);

    return {performerAndCity : performer, eventDate : date, eventUrl : split,
            threshold : threshold, email : email};
}

// sends a post request to url (lambda), sending sendData
function postFetch(url, sendData) {
    fetch(url, {
            method: 'POST',
            body: JSON.stringify(sendData),
            })
            .then((res) => res.json())
            .then((json) => { console.log(json)});
    }

// listener for when Submit button is pressed
// TODO: work out currency into here
function buttonListener() {
    document.getElementById("submit").addEventListener('click', () => {
        const email = document.getElementById("email").value;
        if (!validate(email.toLowerCase(), EMAIL_PATTERN)) {
            alert("Please enter a valid email address");
            return;
        }
        const threshold = Number(document.getElementById("threshold").value);
        if (threshold <= 0 || !Number.isInteger(threshold)) {
            alert("Price threshold must be a positive integer");
            return;
        }
        chrome.tabs.query({ active: true }, function (tabs) {
            const url = tabs[0].url;
            if (url && validate(url, URL_PATTERN)) {
                console.log(url);
                console.log(email);
                console.log(threshold);
                const info = setInfo(url, email, threshold);
                console.log(info);
                postFetch(API, {operation : "insert", info : info});
                alert("Your information has been saved, and you will receive " +
                        "a notification once tickets are available subject to your threshold");
            } else {
                alert("You must be in a StubHub event page operate extension");
            }
        });
    });
}

buttonListener();