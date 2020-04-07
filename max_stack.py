# Implement a class for a stack that supports all the regular
#functions (push, pop) and an additional function of max() which
#returns the maximum element in the stack (return None if the stack is
#empty). Each method should run in constant time.

class MaxStack:
  def __init__(self):
    self.stack = []
    self.max_val = None

  def push(self, val):
    if len(self.stack) == 0:
      self.stack.append(val)
      self.max_val = val
      return
    if val <= self.max_val:
      self.stack.append(val)
      return
    self.stack.append(2*val - self.max_val)
    self.max_val = val

  def pop(self):
    if len(self.stack) == 0:
      return
    if self.stack[-1] < self.max_val:
      self.stack.pop()
      return
    self.max_val = 2 * self.max_val - self.stack[-1] # 2 * max - (2 * max - prev_max) = prev_max
    self.stack.pop()

  def max(self):
    return self.max_val

s = MaxStack()

s.push(1)
s.push(2)
s.push(3)
s.push(2)

print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
