class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value): #time complexity o(1)
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.length += 1

    def prepend(self, value):  #time complexity o(1)
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new
        self.length+=1

    def insert(self,index,value): #rime complexity o(n)
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
    def traversal(self): #time complexity O(n)
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def get(self,index):
        if index == -1:
            return self.tail
        if index < 0 or index >=self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return  True
        return  False




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
new_link.insert(0, +100)
print(new_link)
new_link.traversal()
print(new_link.get(3))

print(new_link.set(2, 50))
print(new_link)




