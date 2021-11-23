var ana = require("./anagram2")
const { test, expect } = require('@jest/globals')
listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

test('anagramsFor() returns list', () => {
    received = ana.anagramsFor('threads', listOfWords)
    expect(received).toBeInstanceOf(Array)
})

test('anagramsFor() returns correct list', () => {
    received = ana.anagramsFor('threads', listOfWords)
    expected = ["threads", "trashed", "hardest", "hatreds"]
    expect(received).toStrictEqual(expected)
})

test('anagramsFor() returns correct list', () => {
    received = ana.anagramsFor('apple', listOfWords)
    expected = []
    expect(received).toStrictEqual(expected)
})
