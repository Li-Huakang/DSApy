# 中缀表达式转后缀表达式
from Stack import Stack


def infix2postfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    postfixlist = []
    tokenlist = infixexpr.split()
    for token in tokenlist:
        if token in "QWERTYUIOPASDFGHJKLZXCVBNM" \
                or token in "1234567890":
            postfixlist.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                postfixlist.append(topToken)
                topToken = opstack.pop()
        else:  # 操作符：栈顶优先级高，反复弹出知道栈顶优先级比他低，将其压入
            while (not opstack.isEmpty()) \
                    and prec[opstack.peek()] >= prec[token]:
                postfixlist.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():  # 把栈清空
        postfixlist.append(opstack.pop())
    return " ".join(postfixlist)


print(infix2postfix("A + B * C / ( A - C ) * B"))
