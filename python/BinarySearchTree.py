from logging import root


class Node:
    def __init__(this, data):
        this.data = data
        this.left = None
        this.right = None

class BinarySearchTree:
    def __init__(this):
        this.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
            return self
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left == None:
                        current.left = newNode
                        return self
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right == None:
                        current.right = newNode
                        return self
                    else:
                        current = current.right



tree = BinarySearchTree()
tree.root = Node(10)
tree.root.right = Node(15)
tree.root.left = Node(7)
tree.root.left.right = Node(9)

print(tree.root)