class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


bt = BinaryTree()

while True:
    print("\n\n1. Insert Book")
    print("2. Search Book")
    print("3. Inorder Traversal")
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        book = input("Enter book name: ")
        bt.root = bt.insert(bt.root, book)
        print("Book inserted successfully.")

    elif ch == 2:
        book = input("Enter book name to search: ")

        if bt.search(bt.root, book):
            print("Book found in catalog.")
        else:
            print("Book not found.")

    elif ch == 3:
        print("Books in alphabetical order:")
        bt.inorder(bt.root)

    elif ch == 4:
        print("Preorder Traversal:")
        bt.preorder(bt.root)

    elif ch == 5:
        print("Postorder Traversal:")
        bt.postorder(bt.root)

    elif ch == 6:
        break

    else:
        print("Invalid choice.")