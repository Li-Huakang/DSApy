from Queue1 import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm #打印速度
        self.currentTask = None #打印任务
        self.timeRemaining = 0 #剩余时间

    def tick(self):#打印1s
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None#一个任务打印结束

    def busy(self):
        if self.currentTask != None:
            return True
        else: return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate

class Task:
    def __init__(self, time):
        self.timestamp = time #生成时间戳
        self.pages = random.randrange(1,21)#随机生成页数

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):#已经等待时间
        return currenttime - self.timestamp

def newPrintTask():#1/181概率生成作业
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:return False


def simulation(pagesPerMinute, numSeconds):#给定ppm和仿真时间
    labprinter = Printer(pagesPerMinute)#创建Printer类，给定ppm
    printQueue = Queue()#创建打印队列
    waitingtimes = []#输出结果记录

    for currentSecond in range(numSeconds):
        if newPrintTask():#生成任务
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):#开始新任务
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()#打印

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print(f"Average Wait {averageWait:6.2f} secs {printQueue.size(): 3d} tasks remaining.")

for i in range(10):
    simulation(5, 3600)