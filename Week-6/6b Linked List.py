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
        print(f"{data} inserted into circular queue")

    def dequeue(self):
        if self.front is None:
            print("Circular Queue Underflow")
            return

        if self.front == self.rear:
            item = self.front.data
            self.front = None
            self.rear = None
        else:
            item = self.front.data
            self.front = self.front.next
            self.rear.next = self.front

        print(f"{item} deleted from circular queue")

    def peek(self):
        if self.front is None:
            print("Circular Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Circular Queue is empty")
            return

        print("Circular Queue elements are:")
        temp = self.front
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.front:
                break

cq_ll = CircularQueueLinkedList()

while True:
    print("\n--- CIRCULAR QUEUE USING LINKED LIST ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter the element to enqueue: "))
        cq_ll.enqueue(item)
    elif choice == 2:
        cq_ll.dequeue()
    elif choice == 3:
        cq_ll.peek()
    elif choice == 4:
        cq_ll.display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice")
