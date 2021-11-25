def balance_parens(str):
    balanced = ''
    open_parens_index = list()
    # loop through entire string
    for char in str:
        # if we have a open parentheses, then we MAY have a close parentheses
        if char == '(':
            open_parens_index.append(len(balanced))  # add index to track

        # if we have a close parentheses, check if we have open parentheses
        elif char == ')':
            if len(open_parens_index) > 0:  # if there is an open
                open_parens_index.pop()  # remove open index
            else:
                continue  # skips closing parentheses

        balanced += char  # append '(' and '[a-zA-Z0-9]'

    if (len(open_parens_index) == 0):
        return balanced

    fully_balanced = ''
    for i, char in enumerate(balanced):  # remove any extra open paras
        if i not in open_parens_index:
            fully_balanced += char

    #  return value will be a string
    return fully_balanced
