#You are given the root of a binary search tree. Return true if it is
#a valid binary search tree, and false otherwise. Recall that a binary
#search tree has the property that all values in the left subtree are
#less than or equal to the root, and all values in the right subtree
#are greater than or equal to the root.

#Here's a starting point:

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def recursive_validate(root, mini, maxi):
  if root is None:
    return True
  if root.key < mini or root.key > maxi:
    return False
  return (recursive_validate(root.left, mini, root.key) and
          recursive_validate(root.right, root.key, maxi))

def is_bst(root):
  return recursive_validate(root, -1e300, 1e300)

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
#1  4 6
