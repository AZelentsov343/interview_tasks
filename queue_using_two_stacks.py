#Hi, here's your problem today. This problem was recently asked by
#Apple:

#Implement a queue class using two stacks. A queue is a data structure
#that supports the FIFO protocol (First in = first out). Your class
#should support the enqueue and dequeue methods like a standard queue.

class Queue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []
    
  def enqueue(self, val):
    self.stack1.append(val)

  def dequeue(self):
    if len(self.stack1) == 0 and len(self.stack2) == 0:
      return None
    if len(self.stack2) == 0:
      while len(self.stack1) != 0:
        self.stack2.append(self.stack1.pop())
    return self.stack2.pop()
      


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
