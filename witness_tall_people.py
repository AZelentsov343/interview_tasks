# There are n people lined up, and each have a height represented as an integer. A
#murder has happened right in front of them, and only people who are taller than
#everyone in front of them are able to see what has happened. How many witnesses are
#there?

#Example:
#Input: [3, 6, 3, 4, 1]  
#Output: 3
#Explanation: Only [6, 4, 1] were able to see in front of them.
'''
 #
 #
 # #
####
####
#####
36341                                 x (murder scene)
'''

def witnesses(heights): #O(n) time O(1) memory
  max = None
  witness_count = 0
  i = len(heights) - 1
  while i >= 0:
    if max is None or heights[i] > max:
      max = heights[i]
      witness_count += 1
    i -= 1
  return witness_count

print(witnesses([3, 6, 3, 4, 1]))
# 3
