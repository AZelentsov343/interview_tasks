# Given a mathematical expression with just single digits, plus signs
#negative signs, and brackets, evaluate the expression. Assume the
#expression is properly formed.

#Example:
#Input: - ( 3 + ( 2 - 1 ) )
#Output: -4

class Solution(object):

  def calculate(self, s): #O(n) time O(n) memory
    arr = [c for c in s if not s.isspace()]
    return self.helper(arr)

  def helper(self, s):
    if len(s) == 0:
      return 0
    stack = []
    sign = '+'
    num = 0
    while len(s) > 0:
      c = s.pop(0)
      if c.isdigit():
        num = num * 10 + int(c)
      if c == '(':
        # do recursion to calculate the sum within the next (...)
        num = self.helper(s)
      if len(s) == 0 or (c == '+' or c == '-' or c == '*' or c == '/' or c == ')'):
        if sign == '+':
          stack.append(num)
        elif sign == '-':
          stack.append(-num)
        elif sign == '*':
          stack[-1] = stack[-1]*num
        elif sign == '/':
          stack[-1] = int(stack[-1]/float(num))
        sign = c
        num = 0
        if sign == ')':
          break
    return sum(stack)


sol = Solution()
print(sol.calculate('- (3 + ( 2 - 1 ) )'))
# -4
print(sol.calculate('1+ -3'))
# -2
