class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        print(value, "inserted")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print(self.queue.pop(0), "deleted")

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue elements:", self.queue)


q = Queue()

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid choice")
