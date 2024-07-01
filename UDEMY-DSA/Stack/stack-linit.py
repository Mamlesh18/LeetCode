class Stack:
    def __init__(self,maxsize):
        self.maxsize = maxsize
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

    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            return "the stack is full"
        else:
            self.list.append(value)
            return "success"
    def pop(self):
        if self.list == []:
            return False
        else:
            self.list.pop()

    def peek(self):
        if self.list == []:
            return False
        else:
            self.list[len(self.list)-1]

    def delete(self):
        self.list = None
stack = Stack(4)
stack.push(10)
stack.push(10)

stack.push(10)
print(stack.pop())

