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
        # checks to see if there is a root already and if there isn't then
        if self.root == None:
            # sets root to newNode then returns the tree
            self.root = newNode
            return self
        # else 
        else:
            # current starts as the current root
            current = self.root
            # while there are still nodes to go through
            while True:
                # checks to see if the data equals a node that's already in the tree. if it is then return None
                if data == current.data:
                    return None
                # if data is is less than the data we currently have, check to see if there is a node to the left
                if data < current.data:
                    # if there is no node on the left, set current.left to the newNode
                    if current.left == None:
                        current.left = newNode
                        return self
                    # if there is a node already, then set current to the node at current.left
                    else:
                        current = current.left
                # if data is more than the data we currently have, check to see if there is a node to the right
                elif data > current.data:
                    # if there is no node on the right, set current.right to the newNode
                    if current.right == None:
                        current.right = newNode
                        return self
                    # if there is a node already, then set current to the node at current.right
                    else:
                        current = current.right

def find(self, data):
    # checks to see if there is a root. if there isn't then return False
    if self.root == None:
        return False
    # if there is a root then check if the data of the new node is the value we're looking for.
    current = self.root
    # set found intially to False to make it easier to return False if we can't find the data
    found = False
    # if it isn't then check to see if the data is greater than or less than the value of the root

    # if it's greater, then check to see if there's a node to the right

    # if it's less, then check to see if there is a node to the left
        
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
tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(5)
tree.insert(2)
tree.insert(16)
tree.insert(7)
# tree.root = Node(10)
# tree.root.right = Node(15)
# tree.root.left = Node(7)
# tree.root.left.right = Node(9)

print(tree.root.data)