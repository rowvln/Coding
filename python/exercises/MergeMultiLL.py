# Create a Node Constructor
class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
    
# Create a LinkedList Constructor
class LinkedList:
    def __init__(self):
        self.head = None

    # Prints method for the Linked List
    def print(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
    
    # flattens multi level double linked lists into a single linked list in order
    def flatten(self, head):
        # if list is empty then return the head
        if not head:
            return head
        # sets current to the head node
        current = head
        # while current is not None, check to see if any nodes have a child
        while current != None:
            # if the node doesn't have a child, move to the next node
            if current.child == None:
                current = current.next
            # else if there is a child, merge the current node with it's child list
            else:
                # sets tail to the child values of the currrent node
                tail = current.child
                # while the tail still has nodes to traverse through the child nodes
                while tail.next != None:
                    # sets rail to the next node in tail
                    tail = tail.next
                # sets the next value of tail to the next node of current
                tail.next = current.next
                # check to see if tail has anymore nodes to traverse through. If there are still nodes, then set the prev value of the node tail.next is pointing to to point to the tail node
                if tail.next != None:
                    tail.next.prev = tail
                # sets the next value of current to the child node
                current.next = current.child
                # sets current.next's prev value to currentls
                current.next.prev = current
                # sets current.child to None
                current.child = None
        return head