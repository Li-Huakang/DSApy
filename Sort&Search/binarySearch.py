#二分法查找有序表
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while  first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

testlist = [1, 3, 10, 20, 36, 50]
print(binarySearch(testlist, 20))

#迭代实现
def binarySearch2(alist, item):

    if len(alist) == 0:
        return False
    else:
        midpoint = (len(alist) - 1)//2
        if item == alist[midpoint]:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch2(alist[:midpoint], item)
            else:
                return binarySearch2(alist[midpoint + 1:], item)

testlist = [1, 3, 10, 20, 36, 50]
print(binarySearch2(testlist, 20))