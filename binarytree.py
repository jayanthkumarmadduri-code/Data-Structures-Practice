class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return True
        elif data < current.data:
            return self._search_recursive(current.left, data)
        else:
            return self._search_recursive(current.right, data)

    def inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):
        if current:
            self._inorder_recursive(current.left)
            print(current.data, end=" ")
            self._inorder_recursive(current.right)

bst = BinarySearchTree()

bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:")
bst.inorder()

print("\nSearch 40:", bst.search(40))
print("Search 100:", bst.search(100))