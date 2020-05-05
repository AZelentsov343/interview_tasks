#Hi, here's your problem today. This problem was recently asked by
#Google:

#You are given the root of a binary tree. Return the deepest node (the
#furthest node from the root).

#Example:

#    a
#   / \
#  b   c
# / 
#d

#The deepest node in this tree is d at depth 3.

class Node(object):  # узел дерева
  def __init__(self, val):
    self.val = val # в узле дерева хранится значение (в нашем случае - буква)
    self.left = None # в узле дерева хранится указатель на левого сына
    self.right = None # в узле дерева хранится указатель на правого сына

  def __repr__(self):
    # string representation
    return self.val


def deepest(node):
  if node is None: # проверка пустого дерева
    return None, 0
  depth = 1 
  queue = [node] # очередь из одного элемента (корень дерева)
  while len(queue) != 1 or queue[0].left is not None or queue[0].right is not None:
    # пока в очереди не останется один бездетный узел
    for _ in range(len(queue)): # для каждого узла в очереди
      if queue[0].left: # если у него есть левый сын, то левый сын встает в очередь
        queue.append(queue[0].left)
      if queue[0].right: #  если у него есть правый сын, то правый сын встает в очередь
        queue.append(queue[0].right)
      queue.pop(0) # отец выходит из очереди
    depth += 1 #на каждой итерации уходит предыдущее поколение и приходит следующее
  return queue[0], depth


# создание дерева и проверка программы на правильность
root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)
