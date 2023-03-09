# Given a linked list, delete the middle node. If the list is even length, delete the node at the start of the second half of the list.
# Uses a singly linked list where you are traversing through the list by using slow and fast pointers. For every one node 'slow' sees, 'fast' will always be one step ahead.
class LLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def deleteMiddleNode(head):
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = slow.next
    else:
        head = head.next
    return head

# prints nodes for testing purposes
def printNodes(head):
    while head:
        print(head.value)
        head = head.next 
    return head

# creates a dummy linked list to test on
node1 = LLNode(4)
node2 = LLNode(7)
node3 = LLNode(2)
node4 = LLNode(5)
node5 = LLNode(1)
node6 = LLNode(3)
node7 = LLNode(8)
node8 = LLNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

printNodes(node1)
print("----------")
deleteMiddleNode(node1)
printNodes(node1)
