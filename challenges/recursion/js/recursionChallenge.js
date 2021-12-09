exports.factorial = (num) => {
    if (num === 0) {
        return 1
    } else {
        return num * this.factorial(num - 1)
    }
};

exports.palindrome = (string) => {
    let word = string.toLowerCase()
    const chars = word.split('').filter((char) => {
        return char.match('[a-z0-9]')
    })
    if (chars.length <= 1) {
        return true
    }
    if (chars[0] !== chars[chars.length - 1]) {
        return false
    }
    return this.palindrome(string.slice(1, string.length - 1))


};

exports.bottles = (num) => {

};

exports.romanNum = function () {

};
