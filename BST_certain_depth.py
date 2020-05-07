#Given a binary tree, return all values given a certain height h.

#Here's a starting point:

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
  cur_depth = 1
  queue = [root]
  while cur_depth < height:
    for i in range(len(queue)):
      if queue[0].left:
        queue.append(queue[0].left)
      if queue[0].right:
        queue.append(queue[0].right)
      queue.pop(0)
    cur_depth += 1
  queue = [a.value for a in queue]
  return queue  

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]
