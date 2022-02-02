// // Javascript Fetch API

// // GET request 
// let request = fetch('some_url');
// request()
//     .then((response) => {
//         if (response.ok) { // status code 200-299
//             doSomething();
//         }
//     });

// // POST request
// let request = fetch('some_url', {
//     method: 'POST',
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify(someData)
// });
// request().then((response) => { }) 

// https://mocki.io/v1/046fa230-c744-491f-8315-588684e9b915

import fetch from 'node-fetch';

async function doFetch(url) {
    try {
        let response = await fetch(url);
        if (!response.ok) { // checks if status is 200-299
            throw response.statusText; // throws error
        }
        let data = await response.json(); // converts stringified to JSON
        return data; // returns a promise with data
    }
    catch (error) { // catch the error
        throw error; // throw the error, again
    }
}

function parseBreakfast(breakfast) {
    return breakfast
        ? `My breakfast today will be ${breakfast.cereal.variety} ${breakfast.cereal.brand} cereal with ${breakfast.milk.milkfat} ${breakfast.milk.type} milk!`
        : "ERROR: Nothing to eat!"
}

url = 'https://mocki.io/v1/046fa230-c744-491f-8315-588684e9b915'
doFetch(url)
    .then((breakfast) => console.log(parseBreakfast(breakfast))) // status 200-299
    .catch((error) => console.log("ERROR: ", error)); // thrown error
