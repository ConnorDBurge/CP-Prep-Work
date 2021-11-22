exports.creditCheck = (string) => {
    const creditNumbers = exports.toList(string) // converts string to list of digits
    const toList = exports.timesTwo(creditNumbers) // doubles each digit in list
    const finalList = exports.sumGT9(toList) // numbers > 9 sum of its own digits
    const sum = exports.sumNumbers(finalList) // get sum  of numbers in list

    if (sum % 10 === 0) {
        return 'The number is valid!'
    }

    return 'The number is invalid!'
}

exports.toList = (creditCardNumbers) => {
    let digitList = []
    for (let i = 0; i < creditCardNumbers.length; i++) {
        let digit = parseInt(creditCardNumbers[i])
        digitList.push(digit)
    }
    return digitList
}

exports.timesTwo = (digitList) => {
    let creditNumbers = []
    for (let i = digitList.length - 1; i >= 0; i--) {
        if (i % 2 === 0) {
            creditNumbers.unshift(digitList[i] * 2)
        } else {
            creditNumbers.unshift(digitList[i])
        }
    }
    return creditNumbers
}

exports.splitDigitsSum = (number) => {
    let digitList = Array.from(number.toString()).map(Number)
    let sum = 0
    for (let i = 0; i < digitList.length; i++) {
        sum += digitList[i]
    }
    return sum
}

exports.sumGT9 = (array) => {
    let finalList = []
    for (let i = 0; i < array.length; i++) {
        if (array[i] > 9) {
            finalList.push(exports.splitDigitsSum(array[i]))
        } else {
            finalList.push(array[i])
        }
    }
    return finalList
}

exports.sumNumbers = (array) => {
    sum = 0
    for (let i = 0; i < array.length; i++) {
        sum += array[i]
    }
    return sum
}