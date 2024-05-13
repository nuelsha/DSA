class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

my_stack = Stack()
my_stack.push("nuel")
my_stack.pop()
print(my_stack.peek())
print(my_stack.is_empty())

