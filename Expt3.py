class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self):
        data = input("Enter book name: ")
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print("Book inserted at beginning.")

    def insert_end(self):
        data = input("Enter book name: ")
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

        print("Book inserted at end.")

    def delete_beginning(self):
        if self.head is None:
            print("List is empty.")
        else:
            print("Deleted book:", self.head.data)
            self.head = self.head.next

    def display(self):
        if self.head is None:
            print("Library catalog is empty.")
        else:
            temp = self.head

            print("Library Catalog:")
            while temp is not None:
                print(temp.data)
                temp = temp.next


l = LinkedList()

while True:
    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        l.insert_beginning()
    elif ch == 2:
        l.insert_end()
    elif ch == 3:
        l.delete_beginning()
    elif ch == 4:
        l.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice.")