class BinaryTreeArray:
    def __init__(self, size=50):
        self.size = size
        self.tree = [None] * size

    def insert_root(self, key):
        self.tree[0] = key

    def set_left(self, key, parent):
        child = 2 * parent + 1
        if parent < self.size and self.tree[parent] is not None:
            if child < self.size:
                self.tree[child] = key
            else:
                print("Index out of range")
        else:
            print("Parent does not exist")

    def set_right(self, key, parent):
        child = 2 * parent + 2
        if parent < self.size and self.tree[parent] is not None:
            if child < self.size:
                self.tree[child] = key
            else:
                print("Index out of range")
        else:
            print("Parent does not exist")

    def preorder(self, index=0):
        if index < self.size and self.tree[index] is not None:
            print(self.tree[index], end=" ")
            self.preorder(2 * index + 1)
            self.preorder(2 * index + 2)

    def inorder(self, index=0):
        if index < self.size and self.tree[index] is not None:
            self.inorder(2 * index + 1)
            print(self.tree[index], end=" ")
            self.inorder(2 * index + 2)

    def postorder(self, index=0):
        if index < self.size and self.tree[index] is not None:
            self.postorder(2 * index + 1)
            self.postorder(2 * index + 2)
            print(self.tree[index], end=" ")

    def levelorder(self):
        for val in self.tree:
            if val is not None:
                print(val, end=" ")

    def display(self):
        for i in range(self.size):
            if self.tree[i] is not None:
                print(f"Index {i}: {self.tree[i]}")

# Driver code
bt = BinaryTreeArray(15)
bt.insert_root("A")
bt.set_left("B", 0)
bt.set_right("C", 0)
bt.set_left("D", 1)
bt.set_right("E", 1)

print("Inorder traversal:")
bt.inorder(0)
print("\nPreorder traversal:")
bt.preorder(0)
print("\nPostorder traversal:")
bt.postorder(0)
print("\nLevelorder traversal:")
bt.levelorder()
