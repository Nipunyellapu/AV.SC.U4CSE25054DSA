class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(value, "pushed")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print(self.stack.pop(), "popped")

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack elements:", self.stack[::-1])


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
