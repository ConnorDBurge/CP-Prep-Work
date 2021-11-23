// Can you translate this driver code to unit tests?
var ana = require("./characterMatch");
const { describe, test, expect } = require('@jest/globals');

test('return type is boolean', () => {
    result = ana.isCharacterMatch('charm', 'march')
    expect(typeof result).toBe('boolean')
})

test('test for `` and ``', () => {
    result = ana.isCharacterMatch('', '')
    expect(result).toBeTruthy()
})

test('test for `` and `march`', () => {
    result = ana.isCharacterMatch('', 'march')
    expect(result).toBeFalsy()
})

test('test for `charm` and `march`', () => {
    result = ana.isCharacterMatch('charm', 'march')
    expect(result).toBeTruthy()
})

test('test for `CharM` and `mARcH`', () => {
    result = ana.isCharacterMatch('CharM', 'mARcH')
    expect(result).toBeTruthy()
})

test('test for `abcde2` and `c2abed`', () => {
    result = ana.isCharacterMatch('abcde2', 'c2abed')
    expect(result).toBeTruthy()
})

test('test for `zach` and `attack`', () => {
    result = ana.isCharacterMatch('zach', 'attack')
    expect(result).toBeFalsy()
})

test('test for `Anna Madrigal` and `A man and a girl`', () => {
    result = ana.isCharacterMatch('Anna Madrigal', 'A man and a girl')
    expect(result).toBeTruthy()
})




// console.log(ana.isCharacterMatch('charm', 'march') === true);
// console.log(ana.isCharacterMatch('zach', 'attack') === false);
// console.log(ana.isCharacterMatch('CharM', 'mARcH') === true);
// console.log(ana.isCharacterMatch('abcde2', 'c2abed') === true);

// console.log("This test is for the challenge quesiton");
// console.log(ana.isCharacterMatch('Anna Madrigal', 'A man and a girl') === true);
