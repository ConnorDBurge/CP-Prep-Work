const { calculateMode } = require('./calculateMode.js');
const { test, expect } = require('@jest/globals');

test('Returns a list', () => {
    received = calculateMode([1, 2, 3, 3])
    expect(received).toBeInstanceOf(Array)
})

test('Returns correct mode', () => {
    received = calculateMode([1, 2, 3, 3])
    expect(received).toStrictEqual([3])
})

test('Returns correct mode', () => {
    received = calculateMode([1, 2, 2, 3, 3])
    expect(received).toStrictEqual([2, 3])
})

test('Returns correct mode', () => {
    received = calculateMode([1, 2, 3])
    expect(received).toStrictEqual([1, 2, 3])
})

test('Returns correct mode', () => {
    received = calculateMode(["who", "what", "where", "who"])
    expect(received).toStrictEqual(["who"])
})

