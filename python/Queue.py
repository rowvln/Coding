class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, first, last, size):
        self.first = None
        self.last = None
        self.size = 0

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

    def dequeue(self):
        if not self.first:
            return None
        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.size -= 1
        return temp.data

