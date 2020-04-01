#You are given a list of numbers, and a target number k. Return
# whether or not there are two numbers in the list that add up to k.
# Try to do it in a single pass of the list.

#Example:
#Given [4, 7, 1 , -3, 2] and k = 5, 
#return true since 4 + 1 = 5.

def two_sum1(l, k): # O(n^2) brute_force
  for i in range(len(l) - 1):
    for j in range(i+1, len(l)):
      if l[i] + l[j] == k:
        return True
  return False

def two_sum2(l, k): #0(n) using set (hash_map)
  prev_set = set()
  for el in l:
    needed = k - el
    if needed in prev_set:
      return True
    prev_set.add(el)
  return False

# Tests
print(two_sum1([4,7,1,-3,2], 5))
# True

print(two_sum1([1, 2, 4], 4))
#False

print(two_sum2([4,7,1,-3,2], 5))
# True

print(two_sum2([1, 2, 4], 4))
#False
