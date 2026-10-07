class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

        print(value, "inserted")

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print(self.queue[self.front], "deleted")

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Front element:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Queue elements:", end=" ")

            i = self.front

            while True:
                print(self.queue[i], end=" ")

                if i == self.rear:
                    break

                i = (i + 1) % self.size

            print()


size = int(input("Enter queue size: "))
q = CircularQueue(size)

while True:
    print("\n--- CIRCULAR QUEUE MENU ---")
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
