const decToRomanModern = [
    { 1000: 'M' },
    { 900: 'CM' },
    { 500: 'D' },
    { 400: 'CD' },
    { 100: 'C' },
    { 90: 'XC' },
    { 50: 'L' },
    { 40: 'XL' },
    { 10: 'X' },
    { 9: 'IX' },
    { 5: 'V' },
    { 4: 'IV' },
    { 1: 'I' }
]

exports.toRoman = function (num) {
    const originalNum = num;
    let romanStr = ''; // string to append to

    for (let obj of decToRomanModern) { // for each obj in array
        let decimal = Object.keys(obj)[0] // store key
        let roman = obj[decimal]; // store value

        let results = Math.floor(num / decimal); // number of times it fits

        for (let i = 0; i < results; i++) {
            romanStr += roman; // append to string 
        }
        num = num % decimal; // subtract amount already appended

        if (num === 0) {
            break; // break when nothing is left over
        }
    }
    return `${originalNum}: ${romanStr}`;
}