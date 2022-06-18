# SinglyLinkedList
# A singly linked list is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node (tail). 
# Each element in a linked list is called a node. 
# A single node contains data and a pointer to the next node which helps in maintaining the structure of the list.

#  piece of data - val
# reference to next node - next

# Creates a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creates a Singly Linked List
# Can only traverse forward through the list. Cannot go backwards and there is no random access to the list. 
# YOU MUST GO THROUGH THE LIST TO GET TO A SPECFIC INDEX IN THE LIST
class SinglyLinkedList:
    # Initializes the Linked List setting head, tail, and length properties
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # SinglyLinkedList - PUSH method
    # This function should accept a Value
    # Create a new node using the value passed to the function
    # If there is no head property on the list, set the head and tail to be the newly created node
    # Otherwise set the next property on the tail to be the new node and set the tail property on the list to be the newly created node
    # Increment the length by one
    # defines a push method where we create a new node in the Linked List and if there is no head property in the list, set the head and tail to be the newly created node.
    # otherwise the next property of the current tail will point to the new node and the current tail will be the new node
    def push(self, data):
        newNode = Node(data)
        # if there is no head in the linked list, set head to the new node and tail to the same head ex. NEW EMPTY LIST: HEAD[]TAIL -> pushing in [1] -> NEW LIST IS NOW: HEAD/TAIL[1]
        if not self.head:
            self.head = newNode
            self.tail = self.head
        # sets current tail to newNode and points tail.next to the newNode ex. LINKED LIST: HEAD[1]-->[2]-->[3]-->[4]TAIL -> pushing in [10] -> LINKED LIST IS NOW: HEAD[1]-->[2]-->[3]-->[4]-->[5]TAIL
        else:
            self.tail.next = newNode
            self.tail = newNode
        # increases length by 1 so you can keep count
        self.length += 1
        # returns the Linked List
        return self

    # Singly LinkedList - POP method
    # This method pops the node at end, decreasing length by 1
    # If there are no nodes in the list, return undefined
    # Loop through the list until you reach the tail
    # Set the next property of the 2nd to last node to be null
    # Set the tail to be the 2nd to last node
    # Decrement the length of the list by 1
    # Return the value of the node removed
    def pop(self):
        # if there are no nodes in the list, return None
        if not self.head:
            return None
        # sets current to the HEAD and newTail to the HEAD
        current = self.head
        newTail = current

        # traverse through the list while while are still nodes to go through. set newTail to the current node and current to the next node in the list.
        while(current.next):
            newTail = current
            current = current.next

        # set the tail to newTail and tail.next to None. decrease length by 1
        self.tail = newTail
        self.tail.next = None
        self.length -= 1

        # if you've popped all of the nodes in the list, reset HEAD and TAIL to None
        if self.length == 0:
            self.head == None
            self.tail == None

        # returns current node
        return current
    
    # Singly LinkedList - SHIFT method
    # Removes a new node from the beginning of a Linked List
    # If there are no nodes, return undefined
    # Store the current head property in a variable 
    # Set the head property to the current head’s next property
    # Decrement the length by 1
    # Return the value of the node removed
    def shift(self):
        # if there are no nodes, return undefined
        if not self.head:
            return None
        # store current head in a variable
        currentHead = self.head
        # sets new head equal to the next element
        self.head = currentHead.next
        self.length -= 1
        # if you've popped all of the nodes in the list, reset TAIL to None
        if self.length == 0:
            self.tail == None
        # returns the element that was removed
        return currentHead

    # Singly LinkedList - UNSHIFT method
    # Adds a new node from the beginning of a Linked List
    # This function should accept a Value
    # Create a new node using the value passed to the function
    # If there is no head property on the list, set the head and tail to be the newly created node
    # Otherwise set the next property on the new node’s head to be the current head and set the head property on the list to be the newly created node
    # Increment the length by one
    # Return the Linked List
    def unshift(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self

    # Singly LinkedList - GET method
    # Retrieves a node by its position in the Linked List
    # This function should accept an index
    # If the index is less than zero or greater than or equal to the length of the list, return None
    # Loop through the list until you reach the index and return the node at that specific index
    def get(self,index):
        # if the index is less than zero or greater than or equal to the length of the list, return None
        if index < 0 or index >= self.length:
            return None
        # set count equal to 0. set current to head
        count = 0
        current = self.head
        # traverses through the linked list to find the index
        while count != index:
            # sets current to the next node
            current = current.next 
            # increases count by 1 until it reaches the index or n-1 length
            count+= 1
        # returns current node
        return current

    # Singly LinkedList - SET method
    # Changing the value of a node based on its position in the Linked List
    # This function should accept a value and an index
    # Use your get function to find the specific node
    # If the node is not found, return false
    # If the node is found, set the value of that node to be the value passed to the function and return true
    def set(self, index, data):
        # checks to see if we can find the node
        foundNode = self.get(index)
        # if we can, then set current data to new data passed. return True
        if foundNode:
            foundNode.data = data
            return True
        # otherwise return False
        else:
            return False

    # Singly LinkedList - INSERT method
    # Adding a node to the Linked List at a specific position
    # If the index is less than zero or greater than the length, return false
    # If the index is the same as the length, push a new node to the end of the list
    # If the index is 0, unshift a new node to the start of the list
    # Otherwise, using the get method, access the node at the index - 1
    # Set the next property on that node to be the new node
    # Set the next property on the new node to be the previous next
    # Increment the length
    # Return true
    def insert(self, index, data):
        # If the index is less than zero or greater than the length, return false
        if index < 0 or index > self.length:
            return False
        # If the index is the same as the length, push a new node to the end of the list
        if index == self.length:
            self.push(data)
            return True
            # return not not self.push(data) <-- utilizes double negation to return the truth value of whether or not the push worked. instead of pushing first then returning True
        # If the index is 0, unshift a new node to the start of the list
        if index == 0:
            self.unshift(data)
            return True
            # return not not self.unshift(data) <-- utilizes double negation to return the truth value of whether or not unshift worked. instead of unshifting first then returning True
        # sets newNode equal to new node with data
        newNode = Node(data)
        # prev is the node at index - 1 length
        prev = self.get(index - 1)
        # temp holds the value of the previous next data
        temp = prev.next
        # sets the next data of the previous node to newNode
        prev.next = newNode
        # sets newNode's next data to the data of the previous node's next value
        newNode.next = temp
        # increase length by 1
        self.length += 1
        # return true
        return True

    # Singly LinkedList - REMOVE method
    # Removing a node from the Linked List at a specific position
    # If the index is less than zero or greater than the length, return None
    # If the index is the same as the length - 1, use pop method
    # If the index is 0, use shift method
    # Otherwise, using the get method, access the node at the index - 1
    # Set the next property on that node to be the next of the next node
    # Decrement the length
    # Return the value of the node removed
    def remove(self,index):
        # If the index is less than zero or equal to or greater than the length, return None
        if index < 0 or index >= self.length:
            return None
        # If the index is equal to 0, use shift method
        if index == 0:
            return self.shift()
        # If the index is equal to length - 1, then use pop method
        if index == self.length - 1:
            return self.pop()
        # previousNode is the node at index - 1 length 
        previousNode = self.get(index - 1)
        # removes holds the value of the previous node's next data
        removed = previousNode.next
        # previousNode's next data is set to removed's next data
        previousNode.next = removed.next
        # decrement length by 1
        self.length -= 1
        # returns removed node
        return removed

    # Singly LinkedList - REVERSE method
    # Reversing the Linked List in place
    # Swap the head and the tail
    # Create a variable called next
    # Create a variable called prev
    # Create a variable called node and initialize it to the head property
    # Loop through the list
    # Set next to be the next property of on whatever node is
    # Sery the next property of the node to be whatever prev is
    # Set prev to be the value of the node variable
    # Set node variable to be the value of the next variable
    def reverse(self):
        # set initial count to 0 for list traversal
        count = 0
        # node is set to the current head
        node = self.head
        # swaps current head with current tail data
        self.head = self.tail
        self.tail = node
        # sets previous and next node to None
        nextNode, prevnode = None, None
        # traverses through the list from left to right
        while count != self.length:
            # sets nextNode equal to the data at the current node's next method
            nextNode = node.next
            # sets current node's next data to previous node
            node.next = prevnode
            # sets previous node to the old head
            prevnode = node
            # sets node to the next node
            node = nextNode
            # increment count by 1
            count += 1
        # returns the reversed LinkedList
        return self

# TESTING CASES HERE FOR ALL THE METHODS FOUND ABOVE
aList = SinglyLinkedList()

aList.push("HELLO")
aList.push("GOODBYE")
aList.push("!")

print("Initial Length " + str(aList.length) + " " + str(aList.head.data))
aList.pop() # Tests popping element at end.
print("New Length " + str(aList.length) + " " + str(aList.head.data)) # PRINTS Hello
aList.shift() # Tests removing element at beginning.
print("New Length " + str(aList.length) + " " + str(aList.head.data)) # Prints GOODBYE
aList.unshift("AYO") # Tests adding element at beginning.
print("New Length " + str(aList.length) + " " + str(aList.head.data)) # Prints AYO
aList.set(0, "YERP")
print("New Length " + str(aList.length) + " " + str(aList.head.data)) # Prints YERP
aList.insert(0, "YAGAH")
print("New Length " + str(aList.length) + " " + str(aList.head.data)) # Prints YAGAH
aList.remove(0)
print("New Length " + str(aList.length) + " " + str(aList.head.data)) # Prints YERP
print("Testing reverse method. here is the current length, head, and tail: " + str(aList.length) + " " + str(aList.head.data) + " & " + str(aList.tail.data)) # Prints 2 YERP & GOODBYE
aList.reverse()
print("Reversed LinkedList with length, head, and tail: " + str(aList.length) + " " + str(aList.head.data) + " & " + str(aList.tail.data)) # Prints 2 GOODBYE & YERP

