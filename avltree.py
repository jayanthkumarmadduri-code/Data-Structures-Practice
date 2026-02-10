class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

class AVL:
    def height(self, n):
        return n.height if n else 0

    def balance(self, n):
        return self.height(n.left) - self.height(n.right)

    def right_rotate(self, y):
        x, T2 = y.left, y.left.right
        x.right, y.left = y, T2
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y, T2 = x.right, x.right.left
        y.left, x.right = x, T2
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.balance(root)

        if b > 1 and key < root.left.key:
            return self.right_rotate(root)
        if b < -1 and key > root.right.key:
            return self.left_rotate(root)
        if b > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if b < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root
        return self.search(root.left, key) if key < root.key else self.search(root.right, key)
avl = AVL()
root = None
for v in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, v)

print("Found" if avl.search(root, 25) else "Not Found")
