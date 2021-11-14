// const arrayToSearchThrough = []; // empty list
// for (let i = 1; i <= 1000; i++) { // pushes 1 . . 1,000 into list
//     arrayToSearchThrough.push(i);
// }

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

