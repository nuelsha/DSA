class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        if self.is_empty():
            self.front = self.rear
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def size(self):
        return self.size


# Example usage:
circular_queue = CircularQueue(5)
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
print("Size of the queue:", circular_queue.size())
print("Dequeue:", circular_queue.dequeue())
print("Dequeue:", circular_queue.dequeue())
print("Size of the queue:", circular_queue.size())
