class Stack:
    def __init__(self):
        self.stack = []

    def push(self):
        book = input("Enter book name: ")
        self.stack.append(book)
        print("Book returned successfully.")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Book issued:", self.stack.pop())

    def display(self):
        if len(self.stack) == 0:
            print("No books in stack.")
        else:
            print("Returned books:")
            for book in reversed(self.stack):
                print(book)


s = Stack()

while True:
    print("\n1. Return Book (Push)")
    print("2. Issue Book (Pop)")
    print("3. Display Books")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        s.push()
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.display()
    elif ch == 4:
        break
    else:
        print("Invalid choice.")