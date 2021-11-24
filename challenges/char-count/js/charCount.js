const charCount = (str) => {
    const counts = {} // creates empty object
    const letters = str.split('').filter((char) => { // splits string into list of characters
        return char !== ' '
    })
    for (let char of letters) { // adds characters to object with count
        counts[char] = isNaN(counts[char]) ? 1 : counts[char] += 1
    }
    return counts // returns the final object
};

module.exports = { charCount }