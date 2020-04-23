#Given a list, find the k-th largest element in the list.
#Input: list = [3, 5, 2, 4, 6, 8], k = 3
#Output: 5

import heapq

def findKthLargest1(nums, k): #(O(n * log(n))) easy way
  nums = sorted(nums)
  return nums[len(nums) - k]

def findKthLargest2(nums, k): #O(n + (n - k)*log(n)) using heap
  heapq.heapify(nums) #O(n)
  for _ in range(len(nums) - k):  #O(n - k)
    heapq.heappop(nums) #O(log(n))
  return nums[0]

for findKthLargest in [findKthLargest1, findKthLargest2]:
  print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
  # 5
