#You are given a positive integer N which represents the number of steps in a staircase. You can
#either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb
#the stairs.
# Can you find a solution in O(n) time?

# How we can see n step in (n + 1)th Fibonacci number

def staircase(n): # beautiful, but O(n^2)
  if n <= 1:
    return 1
  return staircase(n - 2) + staircase(n - 1)
  
def staircase1(n): # O(n) avoid calcutaling more than once
  prev_prev = 0
  prev = 1
  num = 1
  for i in range(n):
    num = prev + prev_prev
    prev_prev = prev
    prev = num
  return num

def staircase2(n): #O(1) just use formula  F_n = {[(√5 + 1)/2] ^ n} / √5
  phi = ((1 + 5 ** 0.5) / 2) ** (n + 1)
  return round(phi / (5 ** 0.5))


print(staircase(4))
# 5
print(staircase(5))
# 8
print(staircase1(4))
# 5
print(staircase1(5))
# 8
print(staircase2(4))
# 5
print(staircase2(5))
# 8
