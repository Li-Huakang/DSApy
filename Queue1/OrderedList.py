from Node import Node
class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()  # 到下一个Node
        return count


    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() >item:
                    stop = True
                else:
                    current = current.getNext()
        return found


    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:#查找插入位置
            if current.getData() > item:
                stop = True
            else:
                previous =current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)



    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:#在第一个需要特殊处理
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

ol = OrderedList()
ol.add(10)
ol.add(20)
ol.add(30)
ol.add(25)
ol.remove(20)
node = ol.head
for i in range(ol.size()):
    print(node.getData())
    node = node.getNext()
print(ol.search(22))