#Given two strings A and B of lowercase letters, return true if and
#only if we can swap two letters in A so that the result equals B.

#Example 1:
#Input: A = "ab", B = "ba"
#Output: true

#Example 2:
#Input: A = "ab", B = "ab"
#Output: false

#Example 3:
#Input: A = "aa", B = "aa"
#Output: true

#Example 4:
#Input: A = "aaaaaaabc", B = "aaaaaaacb"
#Output: true

#Example 5:
#Input: A = "", B = "aa"
#Output: false



class Solution:
  def buddyStrings(self, A, B): # O(n) time O(n) memory
    n = len(A)
    m = len(B)
    s = set()
    unique = True
    if n != m:
      return False
    first_difletter = -1
    second_diflleter = -1
    for i in range(n):
      if first_difletter == -1 and unique:
        if A[i] in s:
          unique = False
          del s
        else:
          s.add(A[i])
      if A[i] != B[i]:
        if first_difletter == -1:
          first_difletter = i
        elif second_diflleter == -1:
          second_diflleter = i
        else:
          return False
    if first_difletter == -1:
      return not unique
    return (A[first_difletter] == B[second_diflleter] and 
            A[second_diflleter] == B[first_difletter])
    


print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
