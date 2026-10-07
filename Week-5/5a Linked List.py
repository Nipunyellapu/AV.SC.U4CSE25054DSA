class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(value, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print(self.top.data, "popped")
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top

            print("Stack elements:", end=" ")

            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

            print()


s = Stack()

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid choice")
