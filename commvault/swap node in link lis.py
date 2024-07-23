class ListNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,val):

        node = ListNode(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length +=1

    def prints(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.value)
            current = current.next
        print(result)

    def swap(self,x,y):
        current = self.head
        result = []
        while current is not None:
            result.append(current.value)
            current = current.next
        for i in range(0,len(result)):
            if result[i] == x:
                result[i] = y
            elif result[i] == y:
                result[i] =x
        print(result)




nodes = Linked()
nodes.append(1)
nodes.append(2)
nodes.append(3)
nodes.append(4)
nodes.append(5)
nodes.append(6)
nodes.append(7)
print(nodes.prints())
print(nodes.swap(3,7))