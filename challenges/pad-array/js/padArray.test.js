const { pad } = require('./padArray.js')
const { expect, test } = require('@jest/globals');

test('Returns a list', () => {
    received = pad([1, 2, 3], 5)
    expect(received).toBeInstanceOf(Array)
})

test('Returns correct list', () => {
    received = pad([1, 2, 3], 3)
    expected = [1, 2, 3]
    expect(received).toStrictEqual(expected)
})

test('Returns correct list', () => {
    received = pad([1, 2, 3], 5)
    expected = [1, 2, 3, null, null]
    expect(received).toStrictEqual(expected)
})

test('Returns correct list', () => {
    received = pad([1, 2, 3], 5, 'apple')
    expected = [1, 2, 3, 'apple', 'apple']
    expect(received).toStrictEqual(expected)
})

test('Returns correct list', () => {
    received = pad([1, 2, 3], 0, 'apple')
    expected = [1, 2, 3]
    expect(received).toStrictEqual(expected)
})