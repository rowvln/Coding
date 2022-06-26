class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, first, last, size):
        self.first = None
        self.last = None
        self.size = 0

    # Enqueue method
    # Adds to the end of the queue. Adds the element to the start of the queue.
    # This function accepts some data
    # Create a new node using the data passed to the function
    # If there are no nodes in the queue, set this node to be the first and last property of the queue
    # Otherwise, set the next property on the current last to be that node, and then set the last property of the queue to be that node
    def enqueue(self, data):
        newNode = Node(data)
        if not self.first:
           self.first = newNode
           self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        
        self.size += 1
        return self.size

    # Dequeue method
    # Removes the first element that was added in. Pops the end element.
    # If there’s no first property, return null
    # Store the first property in a variable
    # See if the first is the same as the last (check if there is only 1 node). If so, set the first and last to be None
    # If there is more than 1 node, set the first property to be the next property of first
    # Decrement the size by 1
    # Return the data of the node dequeued
    def dequeue(self):
        if not self.first:
            return None
        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.size -= 1
        return temp.data

