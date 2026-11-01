class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Preorder Traversal: Root -> Left -> Right
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Inorder Traversal: Left -> Root -> Right
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Postorder Traversal: Left -> Right -> Root
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Level Order Traversal (BFS)
    def levelorder(self, root):
        if root is None:
            return
        queue = [root]
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.data, end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

# Instantiate the tree object
tree = BinaryTree()

# Constructing the tree structure
tree.root = Node("A")
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")

print("Preorder traversal (Root -> Left -> Right):")
tree.preorder(tree.root)

print("\n\nInorder traversal (Left -> Root -> Right):")
tree.inorder(tree.root)

print("\n\nPostorder traversal (Left -> Right -> Root):")
tree.postorder(tree.root)

print("\n\nLevel-order traversal:")
tree.levelorder(tree.root)
