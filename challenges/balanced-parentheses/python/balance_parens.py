def balance_parens(str):
    balanced = ''
    hold = list()

    for x in str:
        if not(x == '(' or x == ')'):
            balanced += x  # adds non parentheses to output

        elif (x == '('):
            balanced += x  # adds open parentheses to output
            hold.append(len(balanced)-1)

        elif (x == ')'):
            if hold != []:
                hold.pop()
                balanced += x

    if len(hold) > 0:
        count = 0
        for x in hold:
            balanced = balanced[0:x-count] + balanced[(x-count+1):]
            count += 1

    return balanced
