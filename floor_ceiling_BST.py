# Given an integer k and a binary search tree, find the floor (less
# than or equal to) of k, and the ceiling (larger than or equal to) of
# k. If either does not exist, then print them as None.

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findFloor(root_node, k):
  if root_node is None:
    return None
  #that means k is in tree, return k 
  if root_node.value == k:
    return k
  elif k < root_node.value: #in this case the floor is definetely in left subtree
    return findFloor(root_node.left, k)
  else: # k > root_node.value.  in this case the floor can be either in right subtree, or in the root
    val = findFloor(root_node.right, k)
    if val is not None and val <= k:
      return val
    else:
      return root_node.value

def findCeil(root_node, k):
  if root_node is None:
    return None
  #that means k is in tree, return k 
  if root_node.value == k:
    return k
  elif k > root_node.value: #in this case the ceiling is definetely in right subtree
    return findCeil(root_node.right, k)
  else: # k < root_node.value.  in this case the ceiling can be either in left subtree, or in the root
    val = findCeil(root_node.left, k)
    if val is not None and val >= k:
      return val
    else:
      return root_node.value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  return findFloor(root_node, k), findCeil(root_node, k)

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)
