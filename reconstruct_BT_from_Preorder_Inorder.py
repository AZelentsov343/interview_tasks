#You are given the preorder and inorder traversals of a binary tree in
#the form of arrays. Write a function that reconstructs the tree
#represented by these traversals.

#Example:
#Preorder: [a, b, d, e, c, f, g]
#Inorder: [d, b, e, a, f, c, g]

#The tree that should be constructed from these traversals is:
#    a
#   / \
#  b   c
# / \ / \
#d  e f  g

from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result

def rec(preorder, inorder):
  assert len(preorder) == len(inorder)
  if len(preorder) == 0:
    return None
  root = Node(preorder[0])
  pos = inorder.index(root.val)
  left_inorder = inorder[:pos]
  right_inorder = []
  if pos + 1 < len(inorder):
    right_inorder = inorder[pos+1:]
  left_preorder = preorder[1:len(left_inorder) + 1]
  right_preorder = []
  if len(left_inorder) + 1 < len(preorder):
    right_preorder = preorder[len(left_inorder)+1:]
  root.left = rec(left_preorder, left_inorder)
  root.right = rec(right_preorder, right_inorder)
  return root

  
def reconstruct(preorder, inorder):
  return rec(preorder, inorder)
  
tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(tree)
# abcdefg
