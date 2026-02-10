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

    def delete(self, key):
        t = self.head
        while t:
            if t.data == key:
                if t.prev:
                    t.prev.next = t.next
                else:
                    self.head = t.next
                if t.next:
                    t.next.prev = t.prev
                return
            t = t.next

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" <-> ")
            t = t.next
        print("None")
dll = DoublyLinkedList()
for v in [10, 20, 30]:
    dll.insert(v)

dll.delete(20)
dll.display()
