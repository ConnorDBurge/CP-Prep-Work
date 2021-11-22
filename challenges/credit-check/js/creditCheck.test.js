// Can you translate this driver code to unit tests?
const { toList, timesTwo, splitDigitsSum, sumGT9, sumNumbers, creditCheck } = require("./creditCheck");
const { describe, expect, test } = require('@jest/globals');

test('creditCheck() returns a string', () => {
    const result = creditCheck('5541808923795240')
    expect(typeof result).toBe('string')
})

test('toList() returns a list', () => {
    const result = toList('5541808923795240')
    expect(result).toBeInstanceOf(Array)
})

test('toList() returns correct list of digits', () => {
    const result = toList('5541808923795240')
    const expectation = [5, 5, 4, 1, 8, 0, 8, 9, 2, 3, 7, 9, 5, 2, 4, 0]
    expect(result).toStrictEqual(expectation)
})

test('timesTwo() returns a list', () => {
    const testArray = [5, 5, 4, 1, 8, 0, 8, 9, 2, 3, 7, 9, 5, 2, 4, 0]
    const result = timesTwo(testArray)
    expect(result).toBeInstanceOf(Array)
})

test('timesTwo() returns correct list of digits doubled', () => {
    const testArray = [5, 5, 4, 1, 8, 0, 8, 9, 2, 3, 7, 9, 5, 2, 4, 0]
    const result = timesTwo(testArray)
    expectation = [10, 5, 8, 1, 16, 0, 16, 9, 4, 3, 14, 9, 10, 2, 8, 0]
    expect(result).toStrictEqual(expectation)
})

test('splitDigitsSum() returns a integer', () => {
    const test = splitDigitsSum(16)
    expect(typeof test).toBe('number')
})

test('splitDigitsSum() returns correct sum of digits', () => {
    const test = splitDigitsSum(16)
    expect(test).toBe(7)
})

test('sumGT9() returns correct list to be summed', () => {
    const testArray = [10, 5, 8, 1, 16, 0, 16, 9, 4, 3, 14, 9, 10, 2, 8, 0]
    const test = sumGT9(testArray)
    expectation = [1, 5, 8, 1, 7, 0, 7, 9, 4, 3, 5, 9, 1, 2, 8, 0]
    expect(test).toStrictEqual(expectation)
})

test('sumNumbers() returns correct sum', () => {
    const testArray = [1, 5, 8, 1, 7, 0, 7, 9, 4, 3, 5, 9, 1, 2, 8, 0]
    const test = sumNumbers(testArray)
    const expectation = 70
    expect(test).toBe(expectation)
})

// Test cases for valid card numbers
test('creditCheck() returns valid card number', () => {
    const testString = '5541808923795240'
    const test = creditCheck(testString)
    expectation = 'The number is valid!'
    expect(test).toBe(expectation)
})

test('creditCheck() returns valid card number', () => {
    const testString = '4024007136512380'
    const test = creditCheck(testString)
    expectation = 'The number is valid!'
    expect(test).toBe(expectation)
})

test('creditCheck() returns valid card number', () => {
    const testString = '6011797668867828'
    const test = creditCheck(testString)
    expectation = 'The number is valid!'
    expect(test).toBe(expectation)
})

// Test cases for in-valid card numbers
test('creditCheck() returns in-valid card number', () => {
    const testString = '5541801923795240'
    const test = creditCheck(testString)
    expectation = 'The number is invalid!'
    expect(test).toBe(expectation)
})

test('creditCheck() returns in-valid card number', () => {
    const testString = '4024007106512380'
    const test = creditCheck(testString)
    expectation = 'The number is invalid!'
    expect(test).toBe(expectation)
})

test('creditCheck() returns in-valid card number', () => {
    const testString = '6011797668868728'
    const test = creditCheck(testString)
    expectation = 'The number is invalid!'
    expect(test).toBe(expectation)
})
