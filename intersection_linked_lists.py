#You are given two singly linked lists. The lists intersect at some
#node. Find, and return the node. Note: the lists are non-cyclical.

#Example:

#A = 1 -> 2 -> 3 -> 4
#B = 6 -> 3 -> 4 

#This should return 3 (you may assume that any nodes with the same
#value are the same node).

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print(c.val)
      c = c.next

def length(node): #O(n) time
  res = 0
  while node:
    res += 1
    node = node.next
  return res

def intersection1(a, b): #O(n + m + max(n, m)) time, O(1) memory
  len_a = length(a)
  len_b = length(b)
  if len_a > len_b:
    a, b = b, a
    len_a, len_b = len_b, len_a
  d = len_b - len_a
  for i in range(d):
    b = b.next
  while a and b and a != b:
    a = a.next
    b = b.next
  return a

def intersection2(a, b): #O(n + m + intersection) time, O(n + m) memory
  arr_a = []
  arr_b = []
  while a and b:
    arr_a.append(a)
    arr_b.append(b)
    a = a.next
    b = b.next
  while a:
    arr_a.append(a)
    a = a.next
  while b:
    arr_b.append(b)
    b = b.next
  i = len(arr_a) - 1
  j = len(arr_b) - 1
  while arr_a[i].val == arr_b[j].val:
    i -= 1
    j -= 1
  return arr_a[i + 1]
  
for intersection in [intersection1, intersection2]:
  a = Node(1)
  a.next = Node(2)
  a.next.next = Node(3)
  a.next.next.next = Node(4)

  b = Node(6)
  b.next = a.next.next

  c = intersection(a, b)
  c.prettyPrint()
  # 3 4
  print()
