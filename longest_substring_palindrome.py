# Find the longest palindrome substring in a given string
#Input: "banana"
#Output: "anana"

#Input: "million"
#Output: "illi"
import numpy as np

class Solution1: # O(n^3) Brute Force
    def isPalindrome(self, s):
      for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
          return False
      return True
    
    def get_all_substr(self, test_str):
      return [test_str[i: j] for i in range(len(test_str))  for j in range(i + 1, len(test_str) + 1)]

    def longestPalindrome(self, s):
      substr = self.get_all_substr(s)
      substr.sort(key=lambda s : len(s), reverse=True)
      for s in substr:
        if self.isPalindrome(s):
          return s


class Solution2: # O(n^2) Expanding from points
    def expand_borders(self, s, left, right):
      if s == '' or left < 0 or right >= len(s) or s[left] != s[right]:
        return 0, ''
      while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
        left -= 1
        right += 1
      return right - left + 1, s[left:right+1]
    
    def longestPalindrome(self, s):
      longest = ''
      for i in range(len(s)):
        length, pal = self.expand_borders(s, i, i+1)
        if length > len(longest):
          longest = pal
        length, pal = self.expand_borders(s, i, i)
        if length > len(longest):
          longest = pal
      return longest


class Solution3: #O(n) Manacher

  def expand_borders(self, s, left, right, odd):
    if left < 0 or right >= len(s):
      return int(odd)
    if (not odd) and s[left] != s[right]:
      return 0
    while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
      left -= 1
      right += 1
    return (right - left + 1)//2

  def odd_substr(self, s):
    d = [0] * len(s)
    left = 0
    right = -1
    for i in range(len(s)):
      k = 0
      if i <= right:
        k = min(right - i, d[right - i + left])
      d[i] = self.expand_borders(s, i - k, i + k, True)
      if (i + d[i] > right):
        left = i - d[i]
        right = i + d[i]
    return np.max(d), np.argmax(d)

  def even_substr(self, s):
    d = [0] * len(s)
    left = 0
    right = -1
    for i in range(len(s)):
      k = 0
      if i <= right:
        k = min(right - i + 1, d[right - i + left + 1])
      d[i] = self.expand_borders(s, i - k - 1, i + k, False)
      if i + d[i] - 1 > right:
        left = i - d[i]
        right = i + d[i] - 1
    return np.max(d), np.argmax(d)

  
  def longestPalindrome(self, s):
    odd_max, odd_num = self.odd_substr(s)
    even_max, even_num = self.even_substr(s)
    if odd_max >= even_max:
      return s[odd_num-odd_max:odd_num+odd_max+1]
    else:
      return s[even_num-even_max:even_num+even_max]

        
# Test program
s = "tracecars"
print(str(Solution3().longestPalindrome(s)))
# racecar
