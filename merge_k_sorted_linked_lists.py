#Hi, here's your problem today. This problem was recently asked by Twitter:

#You are given an array of k sorted singly linked lists. Merge the linked
#lists into a single sorted linked list and return it.


class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists): #O(sum(lenghts) * count)
  if len(lists) == 0:
    return None
  result = None
  cur = None
  lists = sorted(lists, key=lambda x: x.val)
  while len(lists) > 0:
    if result is None:
      result = lists[0]
    else:
      cur.next = lists[0]
    cur = lists[0]    
    lists[0] = lists[0].next
    if lists[0] is None:
      lists.pop(0)
    else:
      i = 1
      while i < len(lists) and lists[0].val > lists[i].val:
        i += 1
      lists.insert(i, lists[0])
      lists.pop(0)
  return result


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456
