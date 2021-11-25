const palindrome = (word) => {
    let string = word.toString().toLowerCase()
    const chars = string.split('').filter((char) => {
        return char.match('[a-z0-9]')
    })

    while (chars.length > 1) {
        if (chars[0] !== chars[chars.length - 1]) {
            return false
        } else {
            chars.pop()
            chars.shift()
        }
    }
    return true
};

module.exports = { palindrome }