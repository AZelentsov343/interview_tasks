#Given a linked list of integers, remove all consecutive nodes that
#sum up to 0.

#Example:
#Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
#Output: 10

#The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that
#sequence should be removed. 4 -> -4 also sums up to 0 too so that
#sequence should also be removed.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node): #O(n) time, O(n) memory
  new_beginning = node
  sums = {}
  cursum = 0
  while node:
    cursum += node.value
    if cursum in sums:
      g = sums[cursum]
      new_sum = cursum
      p = g.next
      g.next = node.next
      while p != node:
        new_sum += p.value
        del sums[new_sum]
        p = p.next
    elif cursum == 0:
      new_sum = 0
      while new_beginning != node:
        new_sum += new_beginning.value
        del sums[new_sum]
        new_beginning = new_beginning.next
      new_beginning = new_beginning.next
    else:
      sums[cursum] = node
    node = node.next
  return new_beginning

#Testing
node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
  print(node.value)
  node = node.next
  # 10
