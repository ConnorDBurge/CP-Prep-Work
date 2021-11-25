const pal = require("./palindrome");
const { expect, test } = require('@jest/globals')

test('Returns a boolean', () => {
    received = pal.palindrome('racecar')
    expect(typeof received).toBe('boolean')
})

test('Returns true', () => {
    received = pal.palindrome('racecar')
    expect(received).toBeTruthy()
})

test('Returns true', () => {
    received = pal.palindrome('Noon')
    expect(received).toBeTruthy()
})

test('Returns true', () => {
    received = pal.palindrome('ciVic')
    expect(received).toBeTruthy()
})

test('Returns true', () => {
    received = pal.palindrome(404)
    expect(received).toBeTruthy()
})

test('Returns true', () => {
    received = pal.palindrome('A man, a plan, a canal -- Panama')
    expect(received).toBeTruthy()
})

test('Returns true', () => {
    received = pal.palindrome('Sore was I ere I saw Eros.')
    expect(received).toBeTruthy()
})

test('Returns false', () => {
    received = pal.palindrome(123)
    expect(received).toBeFalsy()
})

test('Returns false', () => {
    received = pal.palindrome('nice')
    expect(received).toBeFalsy()
})

test('Returns false', () => {
    received = pal.palindrome('bomb')
    expect(received).toBeFalsy()
})


// console.log(pal.palindrome('racecar') === true);
// console.log(pal.palindrome('Noon') === true);
// console.log(pal.palindrome('ciVic') === true);
// console.log(pal.palindrome('nice') === false);
// console.log(pal.palindrome(434) === true);
// console.log(pal.palindrome(123) === false);

// console.log("The following should be true if you're trying to do the extra portion of this challenge");
// console.log(pal.palindrome("Sore was I ere I saw Eros.") === true);
// console.log(pal.palindrome("A man, a plan, a canal -- Panama") === true);
