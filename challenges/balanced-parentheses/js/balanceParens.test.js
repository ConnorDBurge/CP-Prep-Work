const { balanceParens } = require("./balanceParens");

test('Returns string', () => {
    const received = balanceParens('((a(b)c(((')
    expect(typeof received).toBe('string')
})

test('Returns empty string', () => {
    const received = balanceParens('')
    const expected = ''
    expect(received).toStrictEqual(expected)
})

test('Returns correct string', () => {
    const received = balanceParens('((a(b)c(((')
    const expected = 'a(b)c'
    expect(received).toStrictEqual(expected)
})

test('Returns correct string', () => {
    const received = balanceParens('abc(d)e(fgh))(i)j)k')
    const expected = 'abc(d)e(fgh)(i)jk'
    expect(received).toStrictEqual(expected)
})

test('Returns correct string', () => {
    const received = balanceParens('((')
    const expected = ''
    expect(received).toStrictEqual(expected)
})

test('Returns correct string', () => {
    const received = balanceParens('))')
    const expected = ''
    expect(received).toStrictEqual(expected)
})