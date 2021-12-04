const sp = require("./stockPicker");
const { test, expect } = require('@jest/globals')

test('Returns a list', () => {
    expect(sp.picker([17, 3, 6, 9, 15, 8, 6, 1, 10])).toBeInstanceOf(Array)
})

test('Returns correct list', () => {
    expect(sp.picker([17, 3, 6, 9, 15, 8, 6, 1, 10])).toStrictEqual([1, 4])
})

test('Returns correct list', () => {
    expect(sp.picker([3, 17, 6, 9, 18, 15, 6, 1, 10])).toStrictEqual([0, 4])
})

test('Returns correct list', () => {
    expect(sp.picker([1, 17, 6, 9, 8, 15, 6, 3, 19])).toStrictEqual([0, 8])
})

test('Returns correct list', () => {
    expect(sp.picker([19, 17, 6, 9, 8, 15, 6, 3, 1])).toStrictEqual([2, 5])
})


// console.log(shallowEqualArrays(sp.picker([17, 3, 6, 9, 15, 8, 6, 1, 10]), [1, 4]))
// console.log(shallowEqualArrays(sp.picker([17, 3, 6, 9, 15, 8, 6, 1, 10]), [1, 4]))
// console.log(shallowEqualArrays(sp.picker([3, 17, 6, 9, 18, 15, 6, 1, 10]), [0, 4]))
// console.log(shallowEqualArrays(sp.picker([1, 17, 6, 9, 8, 15, 6, 3, 19]), [0, 8]))
// console.log(shallowEqualArrays(sp.picker([19, 17, 6, 9, 8, 15, 6, 3, 1]), [2, 5]))
