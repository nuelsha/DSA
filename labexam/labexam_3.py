class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if self.out_stack:
            return self.out_stack[-1]
        elif self.in_stack:
            return self.in_stack[0]
        else:
            return None
    def is_empty(self):
        return not (self.in_stack or self.out_stack)
    

my_queue = Queue()
my_queue.enqueue("nuelA")
my_queue.dequeue()