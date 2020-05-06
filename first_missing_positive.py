#You are given an array of integers. Return the smallest positive #integer that is not present in the array. The array may contain #duplicate entries.

#For example, the input [3, 4, -1, 1] should return 2 because it is #the smallest positive integer that doesn't exist in the array.

#Your solution should run in linear time and use constant space.

#Here's your starting point:


def first_missing_positive(nums): # O(n) time O(1) memory
  j = 0
  for i in range(len(nums)):
    if nums[i] <= 0:
      nums[i], nums[j] = nums[j], nums[i]
      j += 1
    if len(nums) == j:
      return 1
  
  for i in range(j, len(nums)):
    if abs(nums[i]) < len(nums) - j + 1 and nums[abs(nums[i]) - 1 + j] > 0:
      nums[abs(nums[i]) - 1 + j] = -nums[abs(nums[i]) - 1 + j]
  
  for i in range(j, len(nums)):
    if nums[i] > 0:
      return i + 1 - j
  return len(nums) - j + 1

  
print(first_missing_positive([3, 4, -1, 1]))
# 2
