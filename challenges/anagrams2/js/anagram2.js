const characterMatch = (string1, string2) => {
    // get raw characters with no whitespace
    const string1list = string1.split('').filter((char) => {
        return char !== ' '
    })
    const string2list = string2.split('').filter((char) => {
        return char !== ' '
    })

    // first, check len of strings
    if (string1list.length === string2list.length) {
        // checks characters in strings
        for (let i = 0; i < string1list.length; i++) {
            for (let j = 0; j < string2list.length; j++) {
                if (!string2list.includes(string1list[i])) {
                    return false // false when different char is found
                }
            }
        }
        return true
    }
    return false // returns if strings are not equal size
}


const anagramsFor = (word, listOfWords) => {
    // uses logic from anagrams1 challenge to perform anagram test
    anagrams = listOfWords.filter(ana => characterMatch(word, ana))
    return anagrams
}

module.exports = { anagramsFor }