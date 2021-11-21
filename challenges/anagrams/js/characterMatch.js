exports.isCharacterMatch = function (string1, string2) {

    // get raw characters with no whitespace
    string1list = stringStripper(string1.toLowerCase())
    string2list = stringStripper(string2.toLowerCase())

    // first, check len of strings
    if (string1list.length === string2list.length) {
        // checks characters in strings
        for (let i = 0; i < string1list.length; i++) {
            for (let j = 0; j < string2list.length; j++) {
                if (string2list.includes(string1list[i])) {
                    continue
                } else {
                    return false
                }
            }
        }
        return true
    }
    return false
}


const stringStripper = (string) => {
    result = string.split('')
    stripped = []
    for (let i = 0; i < result.length; i++) {
        if (result[i] !== ' ') {
            stripped.push(result[i])
        }
    }
    return stripped
}
