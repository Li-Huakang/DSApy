# 检查变位词，如：heart和earth，python和typhon
def anagramSolution1(s1, s2):  # 逐字检查法
    alist = list(s2)  # 如果在s2中找到s1中得字母，就将s2该位删去
    pos1 = 0
    stillOK = True  # 判断是否是变位词
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True  # 在s2逐个对比
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None  # 找到，打勾
        else:
            stillOK = False
        pos1 = pos2 + 1
    return stillOK
# 1 + 2 + 3 + ... + n -> O(n^2)

print(anagramSolution1('abcd', 'bcaf'))


def anagramSolution2(s1, s2):  # 排序对比
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches
#排序数量级O(n log n)

print(anagramSolution2('absd', 'bads'))


def anagramSolution3(s1, s2):  # 计数比较
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s1[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False
    return stillOK
#O(n)以空间换时间

print(anagramSolution3('apple', 'pleap'))
