class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, id, name):
        if root is None:
            return Node(id, name)

        if id < root.id:
            root.left = self.insert(root.left, id, name)
        elif id > root.id:
            root.right = self.insert(root.right, id, name)
        else:
            print("Admission ID already exists.")

        return root

    def search(self, root, id):
        if root is None:
            return None

        if root.id == id:
            return root
        elif id < root.id:
            return self.search(root.left, id)
        else:
            return self.search(root.right, id)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.id, "-", root.name)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.id, "-", root.name)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.id, "-", root.name)


bst = BST()

while True:
    print("\n1. Insert Student")
    print("2. Search Student")
    print("3. Inorder Traversal")
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        id = int(input("Enter Admission ID: "))
        name = input("Enter Student Name: ")

        bst.root = bst.insert(bst.root, id, name)
        print("Student record inserted.")

    elif ch == 2:
        id = int(input("Enter Admission ID to search: "))

        result = bst.search(bst.root, id)

        if result:
            print("Student Found!")
            print("Admission ID:", result.id)
            print("Student Name:", result.name)
        else:
            print("Student not found.")

    elif ch == 3:
        print("\nStudent Records (Ascending Order):")
        bst.inorder(bst.root)

    elif ch == 4:
        print("\nPreorder Traversal:")
        bst.preorder(bst.root)

    elif ch == 5:
        print("\nPostorder Traversal:")
        bst.postorder(bst.root)

    elif ch == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")