// Can you translate this driver code to unit tests?
var arm = require("./armstrongNumbers");
let { describe, expect, test } = require('@jest/globals');

function createArrayOfNum(maxValue) { // creates an array 0 to maxValue
  return Array.apply(null, { length: maxValue }).map(Number.call, Number)
}

// Unit Test for findArmstrongNumbers()
test('return type list', () => {
  array = createArrayOfNum(0)
  result = arm.findArmstrongNumbers(array)
  expect(result).toBeInstanceOf(Array);
})

test('return 14 elements in list', () => {
  array = createArrayOfNum(14)
  result = array.length
  expect(result).toEqual(14)
})

test('return an empty list', () => {
  array = createArrayOfNum(0)
  result = arm.findArmstrongNumbers(array)
  expectation = []
  expect(result).toEqual(expectation)
})

test('return armstrong numbers between 0 - 8', () => {
  array = createArrayOfNum(8)
  result = arm.findArmstrongNumbers(array)
  expectation = [0, 1, 2, 3, 4, 5, 6, 7]
  expect(result).toEqual(expectation)
})

test('return armstrong numbers between 0 - 99', () => {
  array = createArrayOfNum(99)
  result = arm.findArmstrongNumbers(array)
  expectation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  expect(result).toEqual(expectation)
})

test('return armstrong numbers between 0 - 999', () => {
  array = createArrayOfNum(999)
  result = arm.findArmstrongNumbers(array)
  expectation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
  expect(result).toEqual(expectation)
})

test('return armstrong numbers between 0 - 9,999', () => {
  array = createArrayOfNum(9999)
  result = arm.findArmstrongNumbers(array)
  expectation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]
  expect(result).toEqual(expectation)
})

