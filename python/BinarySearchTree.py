class Node:
    def __init__(this, data):
        this.data = data
        this.left = None
        this.right = None

class BinarySearchTree:
    def __init__(this):
        this.root = None

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

tree = BinarySearchTree()
tree.root = Node(10)
tree.root.right = Node(15)
tree.root.left = Node(7)
tree.root.left.right = Node(9)

print(int(tree.root))