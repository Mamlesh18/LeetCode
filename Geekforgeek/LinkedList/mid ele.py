class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,val):
        new = Node(val)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.length+=1

    def middle(self):
        result = 0
        current = self.head

        mid = self.length//2
        for i in range(mid+1):
            result = current.value
            current =  current.next

        return result
list = LinkedList()
list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)
list.middle()

