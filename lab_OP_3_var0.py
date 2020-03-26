import sys

oper = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
        '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def parse(formula_string):
    numbers = ''
    for s in formula_string:
        if s in '1234567890.':
            numbers += s
        elif numbers:
            yield float(numbers)
            numbers = ''
        if s in oper or s in "()":
            yield s
    if numbers:
        yield float(numbers)


def calc(polish):
    stack = []
    for token in polish:
        if token in oper:
            y = stack.pop()
            x = stack.pop()
            stack.append(oper[token][1](x, y))
        else:
            stack.append(token)
    return stack[0]


def ShuntingYard(parsed_formulas):
    stack = []
    for token in parsed_formulas:
        if token in oper:
            while stack and stack[-1] != "(" and oper[token][0] <= oper[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)
        elif token == ")":
            while stack:
                x = stack.pop()
            if x == "(":
                break
                yield x
        elif token == "(":
            stack.append(token)
        else:
            yield token
    while stack:
        yield stack.pop()


if len(sys.argv) > 1:
    formulaa = ""
    for i in range(1, len(sys.argv)):
        formulaa = str(formulaa) + str(sys.argv[i])
    print("Result: ",calc(ShuntingYard(parse(formulaa))))
else:
    print("ERROR")