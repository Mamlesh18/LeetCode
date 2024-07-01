class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def sorted(self,value):
        new = Node(value)
        if self.head is None or value < self.head.value:
            new.next = self.head
            self.head = new
            if self.tail is None:
                self.tail = new

            self.length += 1
            return

        current = self.head
        while current.next is not None and current.next.value < value:
            current = current.next

        new.next  = current.next
        current.next = new
        if new.next is None:
            self.tail = new
        self.length +=1


    def merged(self,list1,list2):

        merge = Linked()

        list1 = list1.head
        list2 = list2.head

        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                merge.sorted(list1.value)
                list1 = list1.next
            else:
                merge.sorted(list2.value)
                list2 = list2.next

        while list1 is not None:
            merge.sorted(list1.value)
            list1 = list1.next

        while list2 is not None:
            merge.sorted(list2.value)
            list2 = list2.next
        return merge

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp = temp.next
        return result

new_node1 = Linked()

new_node1.sorted(100)
new_node1.sorted(20)
new_node1.sorted(30)
new_node1.sorted(400)


new_node2 = Linked()

new_node2.sorted(1000)
new_node2.sorted(2)
new_node2.sorted(1)
new_node2.sorted(8)

print(new_node1)
print(new_node2)

merged_list = Linked().merged(new_node1,new_node2)
print(merged_list)

