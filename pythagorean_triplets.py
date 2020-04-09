#Given a list of numbers, find if there exists a pythagorean triplet
#in that list. A pythagorean triplet is 3 variables a, b, c where 
#a2+b2 = c2

#Example:
#Input: [3, 5, 12, 5, 13]
#Output: True
#Here, 5^2 + 12^2 = 13^2.

def findPythagoreanTriplets1(nums): # O(n^2) brute force, but sort first
  nums = sorted(nums) # O(n*log(n))
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      for k in range(j+1, len(nums)):
        if nums[i] ** 2 + nums[j] ** 2 == nums[k] ** 2:
          return True
  return False

def findPythagoreanTriplets2(nums): # O(max * max) time, O(max) memory
  maximum = max(nums)
  hash_map = [0] * (maximum+1)
  for num in nums:
    hash_map[num] += 1
  
  for i in range(maximum+1):
    if hash_map[i] == 0:
      continue
    for j in range(1, maximum+1):
      if hash_map[j] == 0 or i == j:
        continue
      val = int((i ** 2 + j ** 2) ** 0.5)
      if val ** 2 != i ** 2 + j ** 2:
        continue
      if hash_map[val]:
        return True
  return False

print(findPythagoreanTriplets1([3, 12, 5, 13]))
# True
print(findPythagoreanTriplets2([3, 12, 5, 13]))
# True
