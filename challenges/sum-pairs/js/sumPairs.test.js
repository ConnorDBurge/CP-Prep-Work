const sp = require("./sumPairs");
const { detect, expect, test } = require('@jest/globals')

// run test cases using 'npm run test'

test('test an empty list', () => {
    received = sp.sumPairs([], 20)
    expected = 'unable to find pairs'
    expect(received).toStrictEqual(expected)
})

test('returns sum pairs for 9', () => {
    received = sp.sumPairs([1, 2, 3, 4, 5], 9)
    expected = [[4, 5]]
    expect(received).toStrictEqual(expected)
})

test('returns sum pairs for 7', () => {
    received = sp.sumPairs([1, 2, 3, 4, 5], 7)
    expected = [[2, 5], [3, 4]]
    expect(received).toStrictEqual(expected)
})

test('returns no sum paris 27', () => {
    received = sp.sumPairs([3, 1, 5, 8, 2], 27)
    expected = 'unable to find pairs'
    expect(received).toStrictEqual(expected)
})
