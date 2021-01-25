# 检查括号是否符合规则
from Stack import Stack


def parChecker(symbolString):
    s = Stack()
    index = 0
    balenced = True
    while index < len(symbolString) and balenced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if symbol == ')':
                if not s.isEmpty():
                    s.pop()
                else:
                    balenced = False

        index = index + 1

    if balenced and s.isEmpty():
        return True
    else:
        return False


print(parChecker('()(ad)(a)sda()'))
print(parChecker('((())()saac))'))
print(parChecker('((da90)(saac))'))


def parChecker1(symbolString):
    s = Stack()
    index = 0
    balenced = True
    while index < len(symbolString) and balenced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if symbol in ')]}':
                if not s.isEmpty() and isMatch(s.peek(), symbol):
                    s.pop()
                else:
                    balenced = False

        index = index + 1

    if balenced and s.isEmpty():
        return True
    else:
        return False


def isMatch(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)


print(parChecker1('[](){}'))
print(parChecker1('[{(hjsda)da}d]'))
