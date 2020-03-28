#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.

#Input: "((()))"
#Output: True

#Input: "[()]{}"
#Output: True

#Input: "({[)]"
#Output: False

class Solution: # O(n) there might be faster solution, but I didn't found
  def __init__(self):
    self.opening_from_closing = {')': '(', ']': '[', '}': '{'}
    self.openings = set(['(', '{', '['])
  def isValid(self, s):
    stack = []
    for ch in s:
      if ch in self.openings:
        stack.append(ch)
      else: #can use else because string contains nothing but openings and closings
        if stack[-1] == self.opening_from_closing[ch]:
          stack.pop()
        else:
          return False
    if len(stack) == 0:
      return True
    else:
      return False

# Test Program
s = "((()))" 
# should return True
print(Solution().isValid(s))

# Test Program
s = "[()]{}" 
# should return True
print(Solution().isValid(s))

# Test Program
s = "({[)]" 
# should return False
print(Solution().isValid(s))

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
