class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
            return

        temp = self.root
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new
                    break
                else:
                    temp = temp.right

    def search(self, data):
        temp = self.root
        while temp is not None:
            if temp.data == data:
                return True
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def min(self, root):
        temp = root
        while temp.left is not None:
            temp = temp.left
        return temp.data

    def max(self, root):
        temp = root
        while temp.right is not None:
            temp = temp.right
        return temp.data

    def delete(self, root, data):
        if root is None:
            return None

        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            # No child
            if root.left is None and root.right is None:
                return None
            # Only right child
            elif root.left is None:
                return root.right
            # Only left child
            elif root.right is None:
                return root.left
            # Two children
            else:
                temp = self.min(root.right)
                root.data = temp
                root.right = self.delete(root.right, temp)
        return root

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    def count(self, root):
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)

    def height(self, root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
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
bst.inorder(bst.root)

print("\nPreorder:")
bst.preorder(bst.root)

print("\nPostorder:")
bst.postorder(bst.root)

print("\nCount:", bst.count(bst.root))
print("Height:", bst.height(bst.root))

print("Minimum:", bst.min(bst.root))
print("Maximum:", bst.max(bst.root))

print("Search 40:", bst.search(40))
print("Search 100:", bst.search(100))

bst.root = bst.delete(bst.root, 50)

print("\nAfter deleting 50:")
print("Inorder:")
bst.inorder(bst.root)
