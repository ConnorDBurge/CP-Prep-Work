exports.linearSearch = function (valueToFind, arrayToSearchThrough) {
    let index = 0;
    for (let i = 0; i <= arrayToSearchThrough.length; i++) {
        if (valueToFind === arrayToSearchThrough[i]) {
            return index;
        }
        index++;
    }
    return undefined;
};

exports.linearSearchGlobal = function (valueToFind, arrayToSearchThrough) {
    let resultArray = [];
    let index = 0;
    for (let i = 0; i <= arrayToSearchThrough.length; i++) {
        if (valueToFind === arrayToSearchThrough[i]) {
            resultArray.push(index);
        }
        index++;
    }
    return resultArray;
};

