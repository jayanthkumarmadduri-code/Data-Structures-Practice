class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next
        print("None")
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
