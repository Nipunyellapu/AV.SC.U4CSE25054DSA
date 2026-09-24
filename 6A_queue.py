# 6A) Queue - using both Array and Linked List

# ---------------- Queue using Array ----------------
class QueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(data, "enqueued into queue.")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow.")
        else:
            data = self.queue.pop(0)
            print(data, "dequeued from queue.")

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:")
            for i in self.queue:
                print(i)


def run_array_queue():
    q = QueueArray()
    while True:
        print("\n======= QUEUE USING ARRAY =======")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        print("==================================")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            q.enqueue(data)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.peek()
        elif choice == 4:
            q.display()
        elif choice == 5:
            print("Program terminated.")
            break
        else:
            print("Invalid choice.")


# ---------------- Queue using Linked List ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(data, "enqueued into queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow.")
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
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
            while temp is not None:
                print(temp.data)
                temp = temp.next


def run_linkedlist_queue():
    q = QueueLinkedList()
    while True:
        print("\n======= QUEUE USING LINKED LIST =======")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        print("=========================================")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            q.enqueue(data)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.peek()
        elif choice == 4:
            q.display()
        elif choice == 5:
            print("Program terminated.")
            break
        else:
            print("Invalid choice.")


# ---------------- Main Menu ----------------
if __name__ == "__main__":
    while True:
        print("\n=========== QUEUE - CHOOSE IMPLEMENTATION ===========")
        print("1. Queue using Array")
        print("2. Queue using Linked List")
        print("3. Exit")
        print("=======================================================")
        opt = int(input("Enter your choice: "))

        if opt == 1:
            run_array_queue()
        elif opt == 2:
            run_linkedlist_queue()
        elif opt == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
