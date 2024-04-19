class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                print("Queue is empty")
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)


# Example usage:
queue_using_stacks = QueueUsingStacks()
queue_using_stacks.enqueue(1)
queue_using_stacks.enqueue(2)
queue_using_stacks.enqueue(3)
print("Size of the queue:", queue_using_stacks.size())
print("Dequeue:", queue_using_stacks.dequeue())
print("Dequeue:", queue_using_stacks.dequeue())
print("Size of the queue:", queue_using_stacks.size())
