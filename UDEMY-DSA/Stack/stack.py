class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "element added"

    def pop(self):
        if self.isEmpty():
            return "there is no elemetns"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty, there are no elements"
        else:
            # Use len(self.list) instead of len(self,list)
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None

    def size(self):
        return len(self.list)



stack = Stack()

# print(stack.isEmpty())

stack.push(10)
stack.push(20)
stack.push(30)
# print(stack)
# print(stack.pop())
print(stack.size())
print(stack.peek())