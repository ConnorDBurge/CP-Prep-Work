const { factorial, palindrome, bottles } = require('./recursionChallenge')
const { expect, test } = require('@jest/globals')

test('factorial(5) == 120', () => {
    expect(factorial(5)).toBe(120)
})

test('factorial(4) == 24', () => {
    expect(factorial(4)).toBe(24)
})

test('palindrome("racecar") == true', () => {
    expect(palindrome("racecar")).toBe(true)
})

test('palindrome("racer") == false', () => {
    expect(palindrome("racer")).toBe(false)
})
