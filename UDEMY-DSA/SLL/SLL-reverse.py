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

    def search(self,target): #time complexity o(n)
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def rotate(self, k):
        if self.head is None or k == 0:
            return
        k = k % self.length
        if k == 0:
            return

        # Find the new tail node
        new_tail = self.head
        for _ in range(self.length - k - 1):
            new_tail = new_tail.next

        # Set the new head and tail nodes
        new_head = new_tail.next
        new_tail.next = None
        self.tail.next = self.head
        self.head = new_head
        self.tail = new_tail


    def sorted(self,value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = None
            self.head = self.tail = new_node
            self.length += 1
            return

        if value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
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

    def merge(self, list1, list2):
        merged = LinkedList()

        l1 = list1.head
        l2 = list2.head

        while l1 is not None and l2 is not None:
            if l1.value < l2.value:
                merged.append(l1.value)
                l1 = l1.next
            else:
                merged.append(l2.value)
                l2 = l2.next

        while l1 is not None:
            merged.append(l1.value)
            l1 = l1.next

        while l2 is not None:
            merged.append(l2.value)
            l2 = l2.next

        return merged

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp = temp.next
        return result



# Create two linked lists
new_link = LinkedList()
new_link.sorted(1)
new_link.sorted(200)
new_link.sorted(3)
new_link.sorted(11)
new_link.sorted(22)

new_line2 = LinkedList()
new_line2.sorted(10)
new_line2.sorted(20)
new_line2.sorted(30)
new_line2.sorted(2)

# Merge the lists
merged_list = LinkedList().merge(new_link, new_line2)

# Print the merged list
print("merge =>", merged_list)


