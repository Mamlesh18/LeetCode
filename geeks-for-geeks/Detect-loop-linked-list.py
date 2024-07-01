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

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp = temp.next
        return result

    def has_loop(self):
        if self.head is None:
            return False

        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True

        return False

new_val = LinkedList()

new_val.prepend(10)
new_val.prepend(20)
new_val.prepend(30)
new_val.prepend(40)
new_val.prepend(10)
print(new_val)

new_val.head.next.next.next.next.next = new_val.head

if new_val.has_loop():
    print("true")
else:
    print("false")
