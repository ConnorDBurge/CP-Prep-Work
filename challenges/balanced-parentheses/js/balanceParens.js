const balanceParens = (str) => {
    let balanced = ''
    let open_parens_indices = []
    if (str.length === 0) { // if input is empty
        return balanced
    }

    // push all characters to balanced and record index of left open parentheses
    for (let char of str) {
        if (char === '(') {
            open_parens_indices.push(balanced.length) // push to index of '('
        } else if (char === ')') {
            if (open_parens_indices.length > 0) {
                open_parens_indices.pop() // pop open index off
            } else {
                continue // skip close, because there is no open waiting to be closed
            }
        }
        balanced += char // always add char to balanced
    }

    // create new balanced and filter indices for opening parentheses left with no clo
    let final_balance = ''
    for (let i = 0; i < balanced.length; i++) {
        if (!open_parens_indices.includes(i)) { // if index not in open_parens_indices add to final_balance
            final_balance += balanced[i]
        }
    }

    return final_balance
}

module.exports = { balanceParens }

