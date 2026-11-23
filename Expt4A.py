class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

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

bt.root = Node("A")
bt.root.left = Node("B")
bt.root.right = Node("C")
bt.root.left.left = Node("D")
bt.root.left.right = Node("E")
bt.root.right.left = Node("F")
bt.root.right.right = Node("G")

print("Inorder Traversal:")
bt.inorder(bt.root)

print("\nPreorder Traversal:")
bt.preorder(bt.root)

print("\nPostorder Traversal:")
bt.postorder(bt.root)