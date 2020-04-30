#Hi, here's your problem today. This problem was recently asked by Twitter:

#You are given an array of integers. Find the maximum sum of all possible
#contiguous subarrays of the array.

#Example:

#[34, -50, 42, 14, -5, 86]

#Given this input array, the output should be 137. The contiguous subarray
#with the largest sum is [42, 14, -5, 86].

#Your solution should run in linear time.


def max_subarray_sum(arr):
  result = 0
  cursum = 0
  for num in arr:
    cursum += num
    cursum = max(cursum, 0)
    result = max(result, cursum)
  return result

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
