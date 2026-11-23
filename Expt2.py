class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1

    def enqueue(self):
        ticket = input("Enter customer name: ")
        self.queue.append(ticket)
        self.rear += 1
        print("Ticket booked successfully.")

    def dequeue(self):
        if self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Ticket served:", self.queue[self.front])
            self.front += 1

    def display(self):
        if self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Waiting customers:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


q = Queue()

while True:
    print("\n1. Book Ticket (Enqueue)")
    print("2. Serve Customer (Dequeue)")
    print("3. Display Queue")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        q.enqueue()
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.display()
    elif ch == 4:
        break
    else:
        print("Invalid choice.")