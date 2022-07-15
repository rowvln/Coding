# Stack
# Follows a LIFO way of doing things where the Last thing In is the First thing Out.
# Stack usually utilize push() and pop() like in the array implementation to add an element to the top or remove an element from the top
# You can also build a Stack like a Singly Linked List
# If you do, then it will have the following parameters

# first - holds the first element
# last = holds the last element
# size - it stores the length of the Stack

# Creates a Node class
class Node:
    def __init__(self):
        self.first = data
        self.next = None

# Creates a Stack
# Can only traverse forward through the list. Cannot go backwards and there is no random access to the list. 
# YOU MUST GO THROUGH THE LIST TO GET TO A SPECFIC INDEX IN THE LIST
class SinglyLinkedList:
    # Initializes the Linked List setting head, tail, and length properties
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # Stack - PUSH method
    # This function should accept a Value
    # Create a new node using the value passed to the function
    # If there is no head property on the list, set the head and tail to be the newly created node
    # Otherwise set the next property on the tail to be the new node and set the tail property on the list to be the newly created node
    # Increment the length by one
    # defines a push method where we create a new node in the Linked List and if there is no head property in the list, set the head and tail to be the newly created node.
    # otherwise the next property of the current tail will point to the new node and the current tail will be the new node
    def push(self, data):
        newNode = Node(data)
        # if there is no head in the linked list, set head and tail to the new node. ex. NEW EMPTY LIST: HEAD[]TAIL -> pushing in [1] -> NEW LIST IS NOW: HEAD/TAIL[1]
        if not self.first:
            self.first = newNode
            self.last = newNode
        # sets current tail to newNode and points tail.next to the newNode ex. LINKED LIST: HEAD[1]-->[2]-->[3]-->[4]TAIL -> pushing in [10] -> LINKED LIST IS NOW: HEAD[1]-->[2]-->[3]-->[4]-->[5]TAIL
        else:
            temp = self.first
            self.first.next = temp
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
        if not self.first:
            return None
        # sets temp to self.first
        temp = self.first

        # If first is equal to the element next to it
        if(self.first == self.last):
            self.last = None

        self.first = self.first.next
        self.size -= 1

        # returns current node
        return temp.value

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

