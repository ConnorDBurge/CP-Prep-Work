// How can you make this more scalable and reusable later?
exports.findArmstrongNumbers = function (numbers) {
    const armstrong = []
    for (let i = 0; i < numbers.length; i++) {
        // number split into list of digits
        numList = Array.from(i.toString()).map(Number)
        numOfDigits = numList.length // number of digits in number

        sum = 0
        for (const digit of numList) {
            sum = sum + (digit ** numOfDigits)
        }

        if (sum == i) {
            armstrong.push(i)
        }
    }
    return armstrong
}

// helper to run function without test cases
const runArmstrong = (maxValue) => {
    array = Array.apply(null, { length: maxValue }).map(Number.call, Number)
    return this.findArmstrongNumbers(array)
}
// console.log(runArmstrong(9999))