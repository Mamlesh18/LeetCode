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

    def pop_first(self):
        if self.length == 0:
            return None
        pop = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            pop.next = None
            self.length -= 1
        return pop

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


    def pop_specific(self,index):
        if self.length == 0:
            return None
        if index == 0:
            self.head = self.tail = None
        else:
            prev_node = self.get(index - 1)
            pop_node = prev_node.next
            prev_node.next = pop_node.next
            pop_node.next = None

        self.length -= 1
        return pop_node

    def delete_all(self):

        self.head = None
        self.tail = None
        self.length = 0


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
print(new_link.pops())
print(new_link)


