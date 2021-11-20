let { sum, multiply } = require("./hello.js");

test("test that 1 + 3 + 5 == 9", () => {
    expect(sum(1, 3, 5)).toBe(9)
})

test("test that 1 * 3 * 5 == 15", () => {
    expect(multiply(1, 3, 5)).toBe(15)
})

