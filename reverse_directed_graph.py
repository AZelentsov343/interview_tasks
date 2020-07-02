#Given a directed graph, reverse the directed graph so all directed
#edges are reversed. 

#Example:
#Input:
#A -> B, B -> C, A ->C

#Output:
#B->A, C -> B, C -> A


class Node:
  def __init__(self, value):
    self.adjacent = []
    self.value = value

def reverse_graph(graph):
  reverse_gr = dict()
  for _, node in graph.items():
    if node.value not in reverse_gr:
      reverse_gr[node.value] = Node(node.value)
    for other_node in node.adjacent:
      if other_node.value not in reverse_gr:
        reverse_gr[other_node.value] = Node(other_node.value)
      reverse_gr[other_node.value].adjacent.append(node.value)
  return reverse_gr
      


a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

for _, val in reverse_graph(graph).items():
  print(val.value, val.adjacent)
# []
# ['a', 'b']
# ['a']
