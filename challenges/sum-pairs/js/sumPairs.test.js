var sp = require("./sumPairs");
var { detect, expect, test } = require('@jest/globals')

// Don't forget to add your tests :)
test('returns a list object', () => {
    received = sp.sumPairs()
    expected = Array
    expect(received).toBeInstanceOf(expected)
})