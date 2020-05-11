#A unival tree is a tree where all the nodes have the same value.
#Given a binary tree, return the number of unival subtrees in the tree.

#For example, the following tree should return 5:

#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

#The 5 trees are:
#- The three single '1' leaf nodes. (+3)
#- The single '0' leaf node. (+1)
#- The [1, 1, 1] tree at the bottom. (+1)

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Solution:

  def __init__(self):
    self.value = 0
  
  def __is_unival(self, root):
    if root.left is None and root.right is None:
      self.value += 1
      return True, root.val
    elif root.right is None:
      res, left_val = self.__is_unival(root.left)
      un = res and left_val == root.val
      self.value += un
      return un, root.val
    elif root.left is None:
      res, right_val = self.__is_unival(root.right)
      un = res and right_val == root.val
      self.value += un
      return un, root.val
    else:
      left_res, left_val = self.__is_unival(root.left)
      right_res, right_val = self.__is_unival(root.right)
      un = right_res and left_res and left_val == root.val and right_val == root.val
      self.value += un
      return un, root.val
      
  def count_unival_subtrees(self, root):
    self.value = 0
    self.__is_unival(root)
    return self.value

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

s = Solution()
print(s.count_unival_subtrees(a))
# 5
