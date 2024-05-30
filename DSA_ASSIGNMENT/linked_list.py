class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtPos(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 2):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        if current is None:
            raise IndexError("Position out of bounds")
        new_node.next = current.next
        current.next = new_node

    def deleteAtPosition(self, position):
        if self.head is None:
            raise IndexError("Oops, the place you picked is not right for our list.")
        if position == 1:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 2):
            if current is None or current.next is None:
                raise IndexError("Oops, the place you picked is not right for our list.")
            current = current.next
        if current.next is None:
            raise IndexError("")
        current.next = current.next.next

    def deleteAfterNode(self, prev_node):
        if prev_node is None or prev_node.next is None:
            raise ValueError("The given node is invalid ")
        prev_node.next = prev_node.next.next

    def searchNode(self, value):
        current = self.head
        position = 1
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example 
ll = LinkedList()
ll.insertAtPos(10, 1)
ll.insertAtPos(20, 2)
ll.insertAtPos(30, 3)
ll.insertAtPos(15, 2)
ll.printList()
ll.deleteAtPosition(3)
ll.printList()
ll.deleteAfterNode(ll.head)
ll.printList()
print(ll.searchNode(15))
print(ll.searchNode(100))

# Path: stack.py

