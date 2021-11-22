// const sumPairs = (array, number) => {
//     const sum_pairs_list = [] // holds sum pairs

//     for (let i = 0; i < array.length - 1; i++) { // fixed number
//         for (let j = i + 1; j < array.length; j++) { // check number
//             if (array[i] + array[j] === number) {
//                 sum_pairs_list.push([array[i], array[j]])
//             }
//         }
//     }
//     if (sum_pairs_list.length === 0) {
//         return 'unable to find pairs'
//     }
//     return sum_pairs_list
// }

const sumPairs = (array, number) => {
    const sum_pairs_list = [] // holds sum pairs
    const sorted_pairs = array.sort()
    let right = sorted_pairs.length - 1
    let left = 0

    while (left < right) {
        let sum = sorted_pairs[right] + sorted_pairs[left]
        if (sum === number) {
            sum_pairs_list.push([sorted_pairs[left], sorted_pairs[right]])
            right--
        } else if (sum < number) {
            left++
        } else {
            right--
        }
    }
    if (sum_pairs_list.length) {
        return sum_pairs_list
    } else {
        return 'unable to find pairs'
    }
}


module.exports = { sumPairs }