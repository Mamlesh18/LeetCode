class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self,values):
        self.items.append(values)
        return "sucess"

    def dequeue(self):
        if self.isEmpty():
            return "fail"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "fail"
        else:
            return self.items[0]

    def delete(self):
        self.items = None



queue = Queue()

print(queue.isEmpty())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue)

print(queue.dequeue())

print(queue)


print(queue.peek())

print(queue.delete())

