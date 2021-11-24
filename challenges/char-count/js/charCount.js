const charCount = (str) => {
    const counts = {}
    const letters = str.split('').filter((char) => {
        return char !== ' '
    })
    for (let char of letters) {
        counts[char] += 1
        if (isNaN(counts[char])) {
            counts[char] = 1
        }
    }
    return counts
};

module.exports = { charCount }