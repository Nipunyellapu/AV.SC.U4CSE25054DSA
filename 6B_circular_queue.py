# 6B) Circular Queue - using both Array and Linked List

# ---------------- Circular Queue using Array ----------------
class CircularQueueArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow.")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            print(data, "enqueued into queue.")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print(data, "enqueued into queue.")

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow.")
        elif self.front == self.rear:
            data = self.queue[self.front]
            self.front = -1
            self.rear = -1
            print(data, "dequeued from queue.")
        else:
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print(data, "dequeued from queue.")

    def peek(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("Queue elements:")
            i = self.front
            while True:
                print(self.queue[i])
                if i == self.rear:
                    break
                i = (i + 1) % self.size


def run_array_circular_queue():
    size = int(input("Enter size of circular queue: "))
    cq = CircularQueueArray(size)
    while True:
        print("\n======= CIRCULAR QUEUE USING ARRAY =======")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        print("============================================")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            cq.enqueue(data)
        elif choice == 2:
            cq.dequeue()
        elif choice == 3:
            cq.peek()
        elif choice == 4:
            cq.display()
        elif choice == 5:
            print("Program terminated.")
            break
        else:
            print("Invalid choice.")


# ---------------- Circular Queue using Linked List ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
        print(data, "enqueued into queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow.")
        elif self.front == self.rear:
            data = self.front.data
            self.front = None
            self.rear = None
            print(data, "dequeued from queue.")
        else:
            data = self.front.data
            self.front = self.front.next
            self.rear.next = self.front
            print(data, "dequeued from queue.")

    def peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            temp = self.front
            print("Queue elements:")
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.front:
                    break


def run_linkedlist_circular_queue():
    cq = CircularQueueLinkedList()
    while True:
        print("\n======= CIRCULAR QUEUE USING LINKED LIST =======")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        print("==================================================")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            cq.enqueue(data)
        elif choice == 2:
            cq.dequeue()
        elif choice == 3:
            cq.peek()
        elif choice == 4:
            cq.display()
        elif choice == 5:
            print("Program terminated.")
            break
        else:
            print("Invalid choice.")


# ---------------- Main Menu ----------------
if __name__ == "__main__":
    while True:
        print("\n====== CIRCULAR QUEUE - CHOOSE IMPLEMENTATION ======")
        print("1. Circular Queue using Array")
        print("2. Circular Queue using Linked List")
        print("3. Exit")
        print("=======================================================")
        opt = int(input("Enter your choice: "))

        if opt == 1:
            run_array_circular_queue()
        elif opt == 2:
            run_linkedlist_circular_queue()
        elif opt == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
