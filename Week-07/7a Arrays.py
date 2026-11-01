class BST:
    def __init__(self):
        self.tree = [None] * 100

    def insert(self, data):
        i = 0
        while True:
            if self.tree[i] is None:
                self.tree[i] = data
                return
            if data < self.tree[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2

    def search(self, data):
        i = 0
        while i < 100 and self.tree[i] is not None:
            if self.tree[i] == data:
                return True
            if data < self.tree[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2
        return False

    def min(self, i):
        temp = self.tree[i]
        while temp:
            if self.tree[2 * i + 1] is None:
                break
            i = 2 * i + 1
            temp = self.tree[i]
        return temp

    def delete(self, data):
        i = 0
        while i < 100 and self.tree[i] is not None:
            if self.tree[i] == data:
                # No child
                if self.tree[2 * i + 1] is None and self.tree[2 * i + 2] is None:
                    self.tree[i] = None
                    return True
                # Only right child
                elif self.tree[2 * i + 1] is None:
                    self.tree[i] = self.tree[2 * i + 2]
                    self.tree[2 * i + 2] = None
                    return True
                # Only left child
                elif self.tree[2 * i + 2] is None:
                    self.tree[i] = self.tree[2 * i + 1]
                    self.tree[2 * i + 1] = None
                    return True
                # Two children
                else:
                    temp = self.min(2 * i + 2)
                    self.tree[i] = temp
                    j = 2 * i + 2
                    while self.tree[j] != temp:
                        if temp < self.tree[j]:
                            j = 2 * j + 1
                        else:
                            j = 2 * j + 2
                    self.tree[j] = None
                    return True
            elif self.tree[i] > data:
                i = 2 * i + 1
            else:
                i = 2 * i + 2
        return False

    def inorder(self, i):
        if i >= 100 or self.tree[i] is None:
            return
        self.inorder(2 * i + 1)
        print(self.tree[i], end=" ")
        self.inorder(2 * i + 2)

    def preorder(self, i):
        if i >= 100 or self.tree[i] is None:
            return
        print(self.tree[i], end=" ")
        self.preorder(2 * i + 1)
        self.preorder(2 * i + 2)

    def postorder(self, i):
        if i >= 100 or self.tree[i] is None:
            return
        self.postorder(2 * i + 1)
        self.postorder(2 * i + 2)
        print(self.tree[i], end=" ")

    def count(self, i):
        if i >= 100 or self.tree[i] is None:
            return 0
        return 1 + self.count(2 * i + 1) + self.count(2 * i + 2)

    def height(self, i):
        if i >= 100 or self.tree[i] is None:
            return 0
        left = self.height(2 * i + 1)
        right = self.height(2 * i + 2)
        return 1 + max(left, right)

# Main
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder:")
bst.inorder(0)

print("\nPreorder:")
bst.preorder(0)

print("\nPostorder:")
bst.postorder(0)

print("\nCount:", bst.count(0))
print("Height:", bst.height(0))

print("\nSearch 40:", bst.search(40))
print("Minimum:", bst.min(0))

bst.delete(50)

print("\nAfter deleting 50:")
print("Inorder:")
bst.inorder(0)
