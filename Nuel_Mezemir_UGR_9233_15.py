class LinearQueue:

    def __init__(self, capacity):
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.items)

    def enqueue(self, data):
        if self.is_full():
            raise Exception("Queue overflow")
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % len(self.items)
        self.items[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue underflow")
        data = self.items[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.items)
        self.size -= 1
        return data
