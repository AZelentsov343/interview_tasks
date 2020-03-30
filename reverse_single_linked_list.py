#Given a singly-linked list, reverse the list. This can be done
# iteratively or recursively. Can you get both solutions?
#Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
#Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head): # O(n)
    next_node = head
    prev_node = None
    while next_node is not None:
      n = next_node.next
      next_node.next = prev_node
      prev_node = next_node
      next_node = n

  # Recursive Solution      
  def reverseRecursively(self, prev, head): # O(n)
    if head is None:
      return
    n = head.next
    head.next = prev
    self.reverseRecursively(head, n)
      

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseRecursively(None, testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4


# Initialize the test list: 
testHead = ListNode(1)
testTail = testHead

print("Initial list: ")
testHead.printList()
# 1
testHead.reverseIteratively(testHead)
print("List after reversal: ")
testTail.printList()
# 1

print("Initial list: ")
testHead.printList()
# 1
testHead.reverseRecursively(None, testHead)
print("List after reversal: ")
testTail.printList()
# 1
