class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def prepend(self,value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.length +=1



    def pops(self):
        if self.length == 0:
            return None
        pop = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -=1
        return pop

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += '->'
            temp = temp.next
        return result

lis = Linked()
lis.prepend(10)
lis.prepend(20)
lis.prepend(30)
lis.prepend(40)
print(lis)
lis.pops()
print(lis)
