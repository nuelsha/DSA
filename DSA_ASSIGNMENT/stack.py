class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.count

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        if self.isEmpty():
            print("is empty")
            return None
        popped = self.head.data
        self.head = self.head.next
        self.count -= 1
        return popped

    def peek(self):
        if self.isEmpty():
            print("is empty")
            return None
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def clear(self):
        self.head = None
        self.count = 0

    def get_items(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

# Example :
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print("Stack size:", stack.size())
print("Stack items:", stack.get_items())

print("Popped element :", stack.pop())

print("Top element :", stack.peek())

print("items after popping:", stack.get_items())

stack.clear()
print("items after clearing:", stack.get_items())
