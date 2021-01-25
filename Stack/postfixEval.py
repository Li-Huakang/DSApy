# 计算后缀表达式的值
from Stack import Stack


def posfixEval(postfixexpr):
    operandStack = Stack()
    tokenlist = postfixexpr.split()

    for token in tokenlist:
        if token in "1234567890":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    if op == "/":
        return op1 / op2
    if op == "+":
        return op1 + op2
    if op == "-":
        return op1 - op2


print(posfixEval("1 2 * 2 3 - /"))
