class Queue():
    def __init__(self, n):
        self.queue = []
        self.size = n
    def enqueue(self, value):
        if len(self.queue) >= self.size:
            print("Queue Full")
        else:
            self.queue.append(value)
    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.pop(-1) 
        else:
            print("Queue Empty")
    def front(self):
        return self.queue[0]
    def rear(self):
        return self.queue[-1]
    def length(self):
        return len(self.queue)
    def display(self):
        print(self.queue)
    
queue = Queue(10)
queue.enqueue(4)
queue.enqueue(6)
queue.enqueue(2)
queue.enqueue(48)
queue.enqueue(5)
# queue.dequeue()
queue.display()
print(queue.front())
print(queue.rear())
print(queue.length())


# queue.display()