class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.length += 1

    def prepend(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new
        self.length+=1

    def insert(self,index,value):
        new = Node(value)
        if index < 0 or index > 0:
            return False
        elif self.length == 0:
            self.head =  new
            self.tail = new
        elif index == 0:
            new.next = self.head
            self.head = new
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new.next = temp.next
            temp.next = new

        self.length+=1
        return True


    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp = temp.next
        return result


new_link = LinkedList()
new_link.append(10)
new_link.append(20)
new_link.prepend(30)
print(new_link)
new_link.prepend(50)
print(new_link)
new_link.insert(0,100)
print(new_link)





