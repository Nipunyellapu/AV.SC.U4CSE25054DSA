class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create a linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter value: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node

    # 2. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # 3. Insert at end
    def insert_end(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # 4. Insert at a specific index
    def insert_index(self):
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        prev = None
        count = 0

        while temp is not None and count < index:
            prev = temp
            temp = temp.next
            count += 1

        if count != index:
            print("Invalid index")
            return

        prev.next = new_node
        new_node.next = temp

    # 5. Delete at a specific index
    def delete_index(self):
        index = int(input("Enter index to delete: "))

        if self.head is None:
            print("List is empty")
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        prev = None
        count = 0

        while temp is not None and count < index:
            prev = temp
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid index")
            return

        prev.next = temp.next

    # 6. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # 8. Count number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
linked_list = LinkedList()

while True:
    print("\n----- SINGLY LINKED LIST -----")
    print("1. Create a linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at a specific index")
    print("5. Delete at a specific index")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        linked_list.create()

    elif choice == 2:
        linked_list.insert_beginning()

    elif choice == 3:
        linked_list.insert_end()

    elif choice == 4:
        linked_list.insert_index()

    elif choice == 5:
        linked_list.delete_index()

    elif choice == 6:
        linked_list.delete_first()

    elif choice == 7:
        linked_list.delete_last()

    elif choice == 8:
        linked_list.count_nodes()

    elif choice == 9:
        linked_list.display()

    elif choice == 10:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
