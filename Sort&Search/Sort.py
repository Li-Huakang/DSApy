#Bubble Sort
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist
#O(n^2)
alist = [1, 3, 4, 10, 5, 2, 20, 16]
print(bubbleSort(alist))

def selectionSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        posOfMax = 0
        for i in range(passnum):
            if alist[i + 1] > alist[posOfMax]:
                posOfMax = i + 1

        alist[posOfMax], alist[passnum] = alist[passnum], alist[posOfMax]
    return alist
#O(n^2)，减小交换次数
print(selectionSort(alist))

def insertionSort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        while (alist[position - 1] > current_value) and position > 0:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = current_value
    return alist
#仍然是O(n^2)，移动操作的赋值操作小于交换操作（1/3），最好情况列表已排好序O(n)
print(insertionSort(alist))

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount>0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        sublistcount = sublistcount//2
    return alist
#相较插入排序，减少了不必要的比较，因为每趟都是序列更有序，而插入排序法的优势就在于有序数列。
#介于O(n)和O(n^2)之间
def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position>=gap and alist[i - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue
    return alist

print(shellSort(alist))


def mergeSort(alist):#分裂+归并
    if len(alist) > 1:#基本结束条件：序列长度分裂为1
        mid = len(alist)//2

        left = alist[:mid]#分裂减小规模
        right = alist[mid:]

        mergeSort(left)#递归调用
        mergeSort(right)

        ####归并
        i = j = k = 0
        while i < len(left) and j < len(right):#拉链式将左右部分交错归并
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):#处理剩下未归并完的
            alist[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            alist[k] = right[j]
            j = j + 1
            k = k + 1

    return alist

print(mergeSort(alist))

#更Pythonic的实现归并排序的代码
#使用append pop extend实现归并
def merge_sort(lst):
    #结束条件
    if len(lst) <= 1:
        return lst

    #分解问题并递归调用
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    #合并左右半部分
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged
#时间复杂度为O(nlog(n))，但是牺牲了一倍的空间
print(merge_sort(alist))


#快速排序，利用了中值将数据分成两半
#分解+分裂（排序过程在分裂过程中完成）
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)
    return alist

def quickSortHelper(alist, first, last):#first last需要用来确定左右标位置，同时不用将alist切片
    if first<last:#结束条件：只剩下分裂点（中值点）
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):#分裂函数（包含移动操作）
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        #寻找调换的点(左标对应的值比中值大，右标对应的值比中值小，就需要调换)
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1

        #如果两标相错就结束
        if rightmark < leftmark:
            done = True
        #进行调换，左右标位置对应的数据。
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    #中值替换
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    #左边的都比中值小，右边的都比中值大
    return rightmark#返回中值点
#O(nlog(n))
# 极端情况，有一部分始终没有数据，则将比O(n^2)更糟糕
print(quickSort(alist))