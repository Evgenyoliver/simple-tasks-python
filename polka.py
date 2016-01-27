# -*- coding: utf-8 -*-
from collections import deque

def polka_notation(text):
    allowed_ops = "+ - * /".split()
    operands = deque()
    operators = deque()

    functions = {
        0: (lambda op1, op2: op1 + op2),
        1: (lambda op1, op2: op1 - op2),
        2: (lambda op1, op2: op1 * op2),
        3: (lambda op1, op2: op1 / op2 if op2 else None),
    }

    for elem in text.split():
        if elem.isdigit():
            operands.append(int(elem))
        elif elem in allowed_ops:
            operators.append(elem)

    if len(operands) < len(operators):
        raise Exception("Wrong number of arguments")

    while True:
        if len(operands) == 1:
            return operands.pop()

        op1=operands.pop()
        op2=operands.pop()
        operator = operators.popleft()

        result = functions[allowed_ops.index(operator)](op1, op2)
        if result is not None:
            operands.append(result)
        else:
            raise ZeroDivisionError()
