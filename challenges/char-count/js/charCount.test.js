const char = require("./charCount");
const { expect, test } = require('@jest/globals');

test('Returns a dictionary object', () => {
    const received = char.charCount('aaabbc')
    expect(typeof received).toBe('object')
})

test('Returns correct object for simple string', () => {
    const received = char.charCount('aaabbc')
    const expected = {
        'a': 3,
        'b': 2,
        'c': 1
    }
    expect(received).toStrictEqual(expected)
})

test('Returns correct object for complex string', () => {
    const received = char.charCount('an apple a day will keep the doctor away')
    const expected = {
        "a": 6,
        "e": 4,
        "l": 3,
        "p": 3,
        "w": 2,
        "d": 2,
        "o": 2,
        "t": 2,
        "y": 2,
        "k": 1,
        "h": 1,
        "i": 1,
        "c": 1,
        "n": 1,
        "r": 1
    }
    expect(received).toStrictEqual(expected)
})
