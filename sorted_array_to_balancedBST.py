#Hi, here's your problem today. This problem was recently asked by LinkedIn:

#Given a sorted list of numbers, change it into a balanced binary search
#tree. You can assume there will be no duplicate numbers in the list.


from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer


def createBalancedBST(nums):
  if len(nums) == 0:
    return
  median = len(nums) // 2
  root = Node(nums[median])
  root.left = createBalancedBST(nums[:median])
  root.right = createBalancedBST(nums[median+1:])
  return root

print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7
