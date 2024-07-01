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
        new_node = Node(value)
        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            self.length += 1
            return

        current = self.head
        while current.next is not None and current.next.value < value:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node
        self.length += 1


    def merged(self,list1,list2):
        merging = Linked()
        list1 = list1.head
        list2 = list2.head
        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                merging.sorted(list1.value)
                list1 = list1.next
            else:
                merging.sorted(list2.value)
                list2 = list2.next
        while list1 is not None:
            merging.sorted(list1.value)
            list1 = list1.next
        while list2 is not None:
            merging.sorted(list2.value)
            list2 = list2.next
        return merging

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp = temp.next
        return result


k = int(input("enter list"))
overall  = []
for i in range(k):
    new = Linked()
    n = int(input("size of linked list"))
    list1 = list(map(int,input("enter element of linked").split()))[:n]
    for l in list1:
        new.sorted(l)
    overall.append(new)

over = overall[0]
for i in range(1,len(overall)):
    over = over.merged(over,overall[i])
print(over)


