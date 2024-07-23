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

    def sums(self,list2):
        current = self.head
        current2 = list2.head
        result= []
        result2 = []
        while current is not None:
            result.append(current.value)
            current = current.next
        while current2 is not None:
            result2.append(current2.value)
            current2 = current2.next

        a = int(''.join(map(str, result)))
        b = int(''.join(map(str, result2)))
        print(a+b)
node =  LinkedList()
t1 = int(input('enter number of nodes'))
for i in range(t1):
    n1 = int(input('enter number'))
    node.append(n1)
node2 = LinkedList()

t2 = int(input('enter number of node'))
for j in range(t2):
    n2 = int(input('enter number 2'))
    node2.append(n2)



node.sums(node2)
