#Given an array nums, write a function to move all 0's to the end of it while
#maintaining the relative order of the non-zero elements.

#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.

class Solution:
  def moveZeros(self, nums): #O(n) time O(1) memory
    count = 0
    n = len(nums)
    for i in range(n):
      if nums[i]:
        nums[count] = nums[i]
        count += 1
    for i in range(count, n):
      nums[i] = 0

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
