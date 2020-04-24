#You are given an array of integers. Return the largest product that
#can be made by multiplying any 3 integers in the array.

#Example:

#[-4, -4, 2, 8] should return 128 as the largest product can be made
#by multiplying -4 * -4 * 8 = 128.

import numpy as np

def maximum_product_of_three1(lst): #O(n * log(n)) time O(1) memory
  n = len(lst)
  lst = sorted(lst)
  if lst[0] >= 0 or lst[n - 1] <= 0: # non-negtive or non-positive
    return lst[n - 1] * lst[n - 2] * lst[n - 3]
  else:
    return max(lst[0] * lst[1] * lst[n - 1],
               lst[n - 3] * lst[n - 2] * lst[n - 1])


def maximum_product_of_three2(nums): # O(n) time O(1) memory
  min1 = np.inf
  min2 = np.inf
  max1 = -np.inf
  max2 = -np.inf
  max3 = -np.inf
  for num in nums: #O(n)
    #maximum check
    if num >= max1:
      max3 = max2
      max2 = max1
      max1 = num
    elif num >= max2:
      max3 = max2
      max2 = num
    elif num > max3:
      max3 = num
    
    #minimum check
    if num <= min1:
      min2 = min1
      min1 = num
    elif num < min2:
      min2 = num
    
  if min1 >= 0 or max1 <= 0: #non-negative or non-positive
    return max1 * max2 * max3
  else:
    return max(max1 * max2 * max3,
               min1 * min2 * max1)



for maximum_product_of_three in [maximum_product_of_three1,
                                 maximum_product_of_three2]:
  print(maximum_product_of_three([-4, -4, 2, 8]))
  # 128
