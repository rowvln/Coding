class Node:
    def __init__(this, data):
        this.data = data
        this.left = None
        this.right = None

class BinarySearchTree:
    def __init__(this):
        this.root = None

<<<<<<< HEAD
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


=======
# def find(self, value):
#     if self.root == None:
#         return False
#     current = self.root
#     found = False
#     while(current and not found):
        
def bfs(self):
    data = []
    queue = []
    node = self.root

    queue.push(node)

    while len(queue):
        node = queue.shift()
        data.push(node)
        if node.left:
            queue.push(node.left)
        if node.right:
            queue.push(node.right)
    return data
>>>>>>> f195e03e4b7be461438c7ecd0d00dfcf42ba16ae

tree = BinarySearchTree()
tree.root = Node(10)
tree.root.right = Node(15)
tree.root.left = Node(7)
tree.root.left.right = Node(9)

print(tree.root)