def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoin = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoin < minCoins:
                minCoins = numCoin
                knownResults[change] = minCoins
    return minCoins

print(recDC([1, 5, 10, 25], 63, [0]*64))

#动态规划解法，并没有递归调用
def dpchange(coinValueList, change, minCoins, usedCoins):
    #记录每一步添加的硬币。在得到最后的解后，减去选择的硬币币值，回溯到表格之前的部分找零，就能逐步得到每一步所选择的硬币币值
    for cents in range(1, change + 1):
        coinCount = cents#初始化一个最大硬币数
        newcoin = 1#初始化新加的硬币
        for j in [c for c in coinValueList if c <= cents]:#减去每个硬币，查询剩余钱需要的最少硬币数min{1 + mincoins(cents - j)}
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1#最少硬币数
                newcoin = j#这一cents添加的新硬币（记录了j，也就可以算出cent-j，即知道上一级最优解

        minCoins[cents] = coinCount
        usedCoins[cents] = newcoin
    coin = change
    while coin > 0:#打印使用的方案
        print(usedCoins[coin])
        coin = coin - usedCoins[coin]
    return coinCount

print(dpchange([1, 5, 10, 20], 63, [0]*64, [0]*64))
