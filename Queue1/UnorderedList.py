from Node import Node
class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):#增加的是一个Node
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()#到下一个Node
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

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




l = UnorderedList()
l.add(1)
l.add(2)
l.add(1)
l.add(10)
print(l.size())