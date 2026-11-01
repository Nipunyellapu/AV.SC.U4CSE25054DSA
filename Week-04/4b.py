class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter value: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next

                temp.next = new_node
                new_node.prev = temp

    def insert_beginning(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    def insert_end(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_index(self):
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))

        if index == 0:
            new_node = Node(data)

            if self.head:
                new_node.next = self.head
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def delete_value(self):
        value = int(input("Enter value to delete: "))

        temp = self.head

        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        print("Node deleted")

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None

    def count(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


dll = DoublyLinkedList()

while True:
    print("\n1. Create a linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at a specific index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.create()
    elif choice == 2:
        dll.insert_beginning()
    elif choice == 3:
        dll.insert_end()
    elif choice == 4:
        dll.insert_index()
    elif choice == 5:
        dll.delete_value()
    elif choice == 6:
        dll.delete_first()
    elif choice == 7:
        dll.delete_last()
    elif choice == 8:
        dll.count()
    elif choice == 9:
        dll.display()
    elif choice == 10:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
