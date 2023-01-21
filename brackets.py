def balanced_test(brackets):
    opened_brackets = '([{'
    closed_brackets = ')]}'
    stack = []
    for bracket in brackets:
        if bracket in opened_brackets:
            stack.append(bracket)
        elif len(stack) > 0:
            if opened_brackets.index(stack[-1]) == closed_brackets.index(bracket):
                stack.pop()
            else:
                return 'Несбалансированно'
        else:
            return 'Несбалансированно'
    if len(stack) == 0:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'
