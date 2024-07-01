class Queue:
    def __init__(self,maxsize):
        self.items = maxsize * [None]
        self.maxzize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxzize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False


    def enqueue(self,value):
        if self.isFull():
            return 'no'
        else:
            if self.top + 1 == self.maxzize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "success"

    def dequeue(self):
        if self.isEmpty():
            return "No"
        else:
            first = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxzize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first

    def peek(self):
        if self.isEmpty():
            return "no"
        else:
            return self.items[self.start]


    def delete(self):
        self.items = self.maxzize * [None]
        self.top = -1
        self.start = -1





queue = Queue(4)
print(queue.isFull())
print(queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(queue)
print(queue.isFull())

print(queue.dequeue())


print(queue)


print(queue.peek())

print(queue.delete())

print(queue)