# Create a Node Constructor
class Node:
    def __init__(self, val=None, next=None):
      self.val = val
      self.next = next
    
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
  
  # Insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
      
  # Generates a list of numbers
  def generateList(self, num):
    while num > 0:
      self.insert(num)
      num -= 1

  # Reverses the Linked List
  def reverseList(self):
    current = self.head
    prev = None
    nextNode = current.next

    while current:
      current.next = prev
      prev = current
      current = nextNode

      if nextNode:
        nextNode = nextNode.next
        
    self.head = prev
      
  # Reverses a range in the Linked List
  def reverseRange(self, m, n):
    currPos = 1
    start = self.head
    current = self.head

    while currPos < m:
      start = current
      current = current.next
      currPos += 1

    newList = None
    tail = current
    
    while currPos >= m and currPos <= n:
      next = current.next
      current.next = newList
      newList = current
      current = next
      currPos += 1

    start.next = newList
    tail.next = current

    if m > 1:
      return self.head
    else:
      return newList
      
    return self.head

NewList = LinkedList()
NewList.generateList(10)

print("Old List")
NewList.print()
NewList.reverseList()

print("\nNew List")
NewList.print()

print("\nRange List")
NewList.reverseRange(2,7)
NewList.print()