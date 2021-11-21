exports.sumPairs = function (array, number) {
    const sum_pairs_list = [] // holds sum pairs

    for (let i = 0; i < array.length; i++) { // fixed number
        for (let j = 0; j < array.length; j++) { // check number
            if (array[i] + array[j] == number) {
                if (checkArray(sum_pairs_list, [array[j], array[i]])) {
                    return sum_pairs_list
                } else {
                    sum_pairs_list.push([array[i], array[j]])
                }
            }
        }
    }
    if (sum_pairs_list.length === 0) {
        return 'unable to find pairs'
    }
    return sum_pairs_list
}

const checkArray = (array, testArray) => {
    for (let i = 0; i < array.length; i++) { // iterates over each array
        let checker = false // records if arrays at index are the same
        for (let j = 0; j < array[i].length; j++) {  // iterates over array elements
            // if combo of [n1, n2] are found then set checker to true
            if (array[i][j] === testArray[j]) {
                checker = true
                // as soon a new value that is not in array is found, checker is false
            } else {
                checker = false
            }
        }
        if (checker) {
            return true
        }
    }
    return false
}
