# DoublyLinkedList
# A doubly linked list is a type of linked list that is bidirectional, that is, it can be traversed in both directions from head to the last node (tail). 
# Each element in a linked list is called a node. 
# A single node contains data, a pointer to the next node, and a node pointer to the previous node which helps in maintaining the structure of the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Creates a Doubly Linked List
# Can traverse forward and backwards through the list. There is no random access to the list. 
class DoublyLinkedList:
    # Initializes the Linked List setting head, tail, and length properties
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Push Method
    # Create a new node with the value passed to the function
    # If the head property is None set the head and tail to be the newly created node
    # If not, set the next property on the tail to be that node
    # Set the previous property on the newly created node to be the tail
    # Set the tail to be the newly created node
    # Increment the length
    def push(self, data):
        newNode = Node(data)
        # if there is no head in the linked list, set head to the new node and tail to the same head ex. NEW EMPTY LIST: HEAD[]TAIL -> pushing in [1] -> NEW LIST IS NOW: HEAD/TAIL[1]
        if not self.head:
            self.head = newNode
            self.tail = newNode
        # Otherwise, set the next value of the tail to point to the new node and the prev value of the new node to the tail. ex. LIST: HEAD[99] -> pushing in 100 -> HEAD[99] => [100]TAIL
        else:
            self.tail.next = newNode
            newNode.prev = self.tail # <-- this is the difference between singly and doubly because now we have to point prev to the previous node
            self.tail = newNode
        # increase length by 1    
        length += 1
        # returns the LinkedList
        return self

    # Pop Method
    # If there is no head, return undefined
    # Store the current tail in a variable to return later
    # If the length is 1, set the head and tail to be null
    # Update the tail to be the previous Node
    # Set the newTail’s next to null
    # Decrement the length
    # Return the value removed
    def pop(self):
        # if there is no head in the list, return None
        if not self.head:
            return None
        # stores current tail in a variable
        poppedNode = self.tail
        # if length is equal to one then set head and tail to None, popping the single node in the list
        if self.length == 1:
            self.head = None
            self.tail = None
        # point the tail to the previous node. update the next value of the tail to None and the popped node's prev value to None to sever the connection between both nodes
        else:
            self.tail = poppedNode.prev
            self.tail.next = None
            poppedNode.prev = None
        # since you removed a node, decrease length by 1
        length -= 1
        # returns the linked list
        return self
    
    # Shift Method
    # If the length is 0, return None
    # Store the current head property in a variable ( we’ll call it old head)
    # If the length is 1, set head and tail to none
    # Update the head to be the next of the old head
    # Set the head’s prev property to None
    # Set the old head’s next to None
    # Decrement the length 
    # Return the old head
    def shift(self):
        # if the length is 0 which means theres nothing in the list to remove, return None
        if self.length == 0:
            return None
        # stores the value of current head in a variable called oldHead
        oldHead = self.head
        # if there is only one node in the list, sever the link by setting its head and tail values to None
        if self.length == 1:
            self.head = None
            self.tail = None
        # set head to the next value of oldHead. set head's prev value to None and oldHead's next value to None, severing the link between the node that you are moving forward or backwards from
        else:
            self.head = oldHead.next
            self.head.prev = None
            oldHead.next = None
        # decrease length by 1
        length -= 1
        # return the old head youre moving forward or backwards from
        return oldHead

    # Unshift Method
    # Adding a node to the beginning of Doubly Linked list
    # Create a new node with the data passed to the function
    # If the length is 0, set the head and tail to be the new node
    # Otherwise, set the previous property on the head of the list to be the new node. Set the next property on the new node to be the head property. Update the head to be the new node
    # Increment the length
    def unshift(self, data):
        # Creates a new node with the data passed into the function
        newNode = Node(data)
        # if length is 0, set head and tail to the new node
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        # otherwise, set the prev value of the head to be the new node. change the new Node's next value to be the head property. update the head to be the new node
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        # increase length by 1
        length += 1
        # return the list
        return self