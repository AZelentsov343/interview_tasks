#Given an array with n objects colored red, white or blue, sort them
#in-place so that objects of the same color are adjacent, with the
#colors in the order red, white and blue.

#Here, we will use the integers 0, 1, and 2 to represent the color red
#white, and blue respectively.

#Note: You are not suppose to use the library’s sort function for this
#problem.

#Can you do this in a single pass?

#Example:
#Input: [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]


class Solution:
  def sortColors(self, nums):
    lt = 0
    i = 0
    gt = len(nums) - 1
    for v in [0, 1, 2]:
      while (i < gt):
        if nums[i] < v:
          nums[i], nums[lt] = nums[lt], nums[i]
          lt += 1
          i += 1
        elif nums[i] > v:
          nums[i], nums[gt] = nums[gt], nums[i]
          gt -= 1
        else:
          i += 1
      lt = i
      gt = len(nums) - 1
        

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
