class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        n = Node(data)
        if self.head:
            self.head.prev = n
            n.next = self.head
        self.head = n

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" <-> ")
            t = t.next
        print("None")
dll = DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.display()
