# Given an array of n positive integers and a positive integer s, find the minimal length of
#a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

#Example:
#Input: s = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: the subarray [4,3] has the minimal length under the problem constraint.

class Solution1: # O(n^2) time
  def minSubArrayLen(self, nums, s): 
    min_result = 0
    for start in range(len(nums)):
      cursum = nums[start]
      if cursum >= s:
        return 1
      for end in range(start + 1, len(nums)):
        cursum += nums[end]
        if cursum >= s:
          res = end - start + 1
          if min_result == 0 or res < min_result:
            min_result = res
    return min_result

class Solution2: # O(n) time
  def minSubArrayLen(self, nums, s):
    start = 0
    cursum = 0
    min_result = 0
    for i in range(len(nums)):
      cursum += nums[i]
      while cursum >= s and start != i:
        res = i - start + 1
        if res == 1:
          return res
        if min_result == 0 or res <= min_result:
          min_result = res
        cursum -= nums[start]
        start += 1
    return min_result
    
# Mini-testing
for sol in [Solution1(), Solution2()]:
  print(sol.minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
  # 2
