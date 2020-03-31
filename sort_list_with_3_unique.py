#Given a list of numbers with only 3 unique numbers (1, 2, 3), sort
# the list in O(n) time.
# Challenge: Try sorting the list using constant space.

#Input: [3, 3, 2, 1, 3, 2, 1]
#Output: [1, 1, 2, 2, 3, 3, 3]

def sortNums(nums): # O(n) time O(1) space
  counts = [0] * 3
  for num in nums:
    counts[num-1] += 1
  nums[:counts[0]:] = [1] * counts[0]
  nums[counts[0]:counts[0]+counts[1]:] = [2] * counts[1]
  nums[counts[0]+counts[1]:] = [3] * counts[2]

nums = [3, 3, 2, 1, 3, 2, 1]
sortNums(nums)
print(*nums)
# [1, 1, 2, 2, 3, 3, 3]
