#Given a list of numbers, where every number shows up twice except
# for one number, find that one number.
#Challenge: Find a way to do this using O(1) memory.

#Input: [4, 3, 2, 4, 1, 3, 2]
#Output: 1

def singleNumber1(nums): #O(n^2) time O(1) memory: brute force 
  for index, el in enumerate(nums):
    if (not el in nums[:index]) and (not el in nums[index+1:]):
      return el
  return -1

from collections import defaultdict
def singleNumber2(nums): #O(n) time O(n) memory
  hash_map = defaultdict(int)
  for el in nums:
    hash_map[el] += 1
  for key in hash_map.keys():
    if hash_map[key] == 1:
      return key
  return -1

def singleNumber3(nums): #O(n*log(n)) time O(1) memory
  nums = sorted(nums)
  prev = nums[0] - 1
  first_in_pair = True
  for el in nums:
    if not first_in_pair:
      if el != prev:
        return prev
      first_in_pair = True
    else:
      first_in_pair = False
    prev = el
  return -1

def singleNumber4(nums): #O(n) time O(1) memory, most elegant way
  result = 0
  for el in nums:
    result ^= el # here all repeating elements go away after xor
  return result


print(singleNumber1([4, 3, 2, 4, 1, 3, 2]))
# 1

print(singleNumber2([4, 3, 2, 4, 1, 3, 2]))
# 1

print(singleNumber3([4, 3, 2, 4, 1, 3, 2]))
# 1

print(singleNumber4([4, 3, 2, 4, 1, 3, 2]))
# 1
