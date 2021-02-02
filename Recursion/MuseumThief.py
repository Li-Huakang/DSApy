#动态规划解法
treasure = [None,{'w':2, 'v':3}, {'w':3, 'v':4},
            {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]

max_w = 20

m = {(i, w): 0 for i in range(len(treasure))
     for w in range(max_w + 1)}#初始化m(i,w)，i为财物序号，w为重量，m为偷前i个宝物最大价值

for i in range(1, len(treasure)):
    for w in range(1, max_w + 1):
        if treasure[i]['w'] > w:#装不下第i个宝物
            m[(i, w)] = m[(i-1, w)]
        else:
            m[(i,w)] = max(m[(i-1, w)], m[(i-1, w - treasure[i]['w'])] + treasure[i]['v'])

print(m[(len(treasure)-1, max_w)])


#迭代解法
tr = {(2,3), (3,4), (4,8), (5,8), (9,10)}
max_w = 20
m = {}
def thief(tr, w):
    if tr == set() or w == 0:#递归结束条件
        m[(tuple(tr), w)] = 0
        return 0
    elif (tuple(tr), w) in m:#读取已经记忆的结果
        return m[(tuple(tr), w)]
    else:
        vmax = 0
        for t in tr:#逐一拿出一个宝物，递归调用求最大价值
            if t[0] <= w:
                v = thief(tr-{t}, w-t[0]) + t[1]
                vmax = max(vmax, v)
        m[(tuple(tr), w)] = vmax
        return vmax

print(thief(tr, max_w))
print(m)