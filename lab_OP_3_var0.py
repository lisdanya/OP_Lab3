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


