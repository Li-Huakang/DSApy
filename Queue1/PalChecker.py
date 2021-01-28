from pythonds.basic.deque import Deque

def palChecker(aString):
    charDeque = Deque()

    for ch in aString:
        charDeque.addRear(ch)

    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palChecker("上海自来水来自海上"))