class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
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
        self.length += 1


    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head , self.tail = self.tail, self.head

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp = temp.next
        return result


new_val = LinkedList()
new_val.prepend(10)
new_val.prepend(20)
new_val.prepend(30)
new_val.prepend(40)
new_val.prepend(50)

print("actual list - >  ",new_val)

new_val.reverse()

print(new_val)



