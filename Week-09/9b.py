class AVLTreeArray:
    def __init__(self, size=64):
        self.size = size
        self.tree = [None] * size

    def height(self, i=0):
        if i >= self.size or self.tree[i] is None:
            return 0
        left_h = self.height(2 * i + 1)
        right_h = self.height(2 * i + 2)
        return 1 + max(left_h, right_h)

    def balance_factor(self, i):
        if i >= self.size or self.tree[i] is None:
            return 0
        return self.height(2 * i + 1) - self.height(2 * i + 2)

    def get_subtree(self, i):
        """Extracts (relative_index, value) tuples for a subtree."""
        if i >= self.size or self.tree[i] is None:
            return []
        nodes = [(0, self.tree[i])]
        queue = [(i, 0)]
        while queue:
            curr_idx, rel_idx = queue.pop(0)
            left_child = 2 * curr_idx + 1
            right_child = 2 * curr_idx + 2
            if left_child < self.size and self.tree[left_child] is not None:
                queue.append((left_child, 2 * rel_idx + 1))
                nodes.append((2 * rel_idx + 1, self.tree[left_child]))
            if right_child < self.size and self.tree[right_child] is not None:
                queue.append((right_child, 2 * rel_idx + 2))
                nodes.append((2 * rel_idx + 2, self.tree[right_child]))
        return nodes

    def clear_subtree(self, i):
        if i >= self.size or self.tree[i] is None:
            return
        self.clear_subtree(2 * i + 1)
        self.clear_subtree(2 * i + 2)
        self.tree[i] = None

    def right_rotate(self, root_idx):
        left_idx = 2 * root_idx + 1
        new_root = self.tree[left_idx]
        t2_nodes = self.get_subtree(2 * left_idx + 2)
        right_nodes = self.get_subtree(2 * root_idx + 2)
        t1_nodes = self.get_subtree(2 * left_idx + 1)

        self.clear_subtree(root_idx)
        self.tree[root_idx] = new_root

        # Place new right child (old root)
        right_child = 2 * root_idx + 2
        if right_child < self.size:
            self.tree[right_child] = self.tree[root_idx]  # Old root
        # Reconnect T1, T2, and previous right subtree
        self._rebuild_from_list(self.get_inorder_list(0))

    def left_rotate(self, root_idx):
        self._rebuild_from_list(self.get_inorder_list(0))

    def _rebuild_from_list(self, sorted_vals, i=0):
        if not sorted_vals or i >= self.size:
            return
        mid = len(sorted_vals) // 2
        self.tree[i] = sorted_vals[mid]
        self._rebuild_from_list(sorted_vals[:mid], 2 * i + 1)
        self._rebuild_from_list(sorted_vals[mid + 1:], 2 * i + 2)

    def insert(self, key):
        i = 0
        while i < self.size:
            if self.tree[i] is None:
                self.tree[i] = key
                self.rebalance()
                print(f"{key} inserted into AVL tree")
                return
            elif key < self.tree[i]:
                i = 2 * i + 1
            elif key > self.tree[i]:
                i = 2 * i + 2
            else:
                print("Duplicate keys not allowed")
                return
        print("Tree full / Index out of range")

    def rebalance(self):
        vals = self.get_inorder_list(0)
        self.tree = [None] * self.size
        self._rebuild_from_list(vals, 0)

    def search(self, key):
        i = 0
        while i < self.size and self.tree[i] is not None:
            if self.tree[i] == key:
                return True
            elif key < self.tree[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2
        return False

    def delete(self, key):
        if not self.search(key):
            print("Element not found")
            return
        vals = self.get_inorder_list(0)
        vals.remove(key)
        self.tree = [None] * self.size
        self._rebuild_from_list(vals, 0)
        print(f"Element {key} deleted")

    def get_inorder_list(self, i=0):
        if i >= self.size or self.tree[i] is None:
            return []
        return self.get_inorder_list(2 * i + 1) + [self.tree[i]] + self.get_inorder_list(2 * i + 2)

    def inorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def preorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def postorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")

    def display(self):
        print(f"{'Index':<8}{'Data':<8}{'Left':<8}{'Right':<8}{'Height':<8}")
        for i in range(self.size):
            if self.tree[i] is not None:
                left = 2 * i + 1 if (2 * i + 1 < self.size and self.tree[2 * i + 1] is not None) else -1
                right = 2 * i + 2 if (2 * i + 2 < self.size and self.tree[2 * i + 2] is not None) else -1
                h = self.height(i)
                print(f"{i:<8}{self.tree[i]:<8}{left:<8}{right:<8}{h:<8}")

# Menu-driven Driver Program
avl = AVLTreeArray(64)
while True:
    print("\n--- AVL TREE (ARRAY) MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Display")
    print("8. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        val = int(input("Enter value to insert: "))
        avl.insert(val)
    elif choice == 2:
        val = int(input("Enter value to delete: "))
        avl.delete(val)
    elif choice == 3:
        val = int(input("Enter value to search: "))
        print("Found" if avl.search(val) else "Not Found")
    elif choice == 4:
        print("Inorder: ", end="")
        avl.inorder(0)
        print()
    elif choice == 5:
        print("Preorder: ", end="")
        avl.preorder(0)
        print()
    elif choice == 6:
        print("Postorder: ", end="")
        avl.postorder(0)
        print()
    elif choice == 7:
        avl.display()
    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
