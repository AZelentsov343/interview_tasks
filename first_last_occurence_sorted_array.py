#Given a sorted array, A, with possibly duplicated elements, find the
#indices of the first and last occurrences of a target element, x.
#Return -1 if the target is not found.

#Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
#Output: [6,8]

#Input: A = [100, 150, 150, 153], target = 150
#Output: [1,2]

#Input: A = [1,2,3,4,5,6,10], target = 9
#Output: [-1, -1]

class Solution1: #O(n) easy way
  def getRange(self, arr, target):
    left = -1
    right = -1
    for i, el in enumerate(arr):
      if left == -1 and el == target:
        left = i
      elif left != -1 and right == -1 and el != target:
        right = i - 1
        break
    if left != -1 and right == -1:
      right = len(arr) - 1
    return [left, right]


class Solution2: #O(log(n)) efficient way
  def find_left(self, arr, target, low, high):
    if low == high and arr[low] != target:
      return -1
    mid = low + (high - low) // 2
    if (mid == 0 or arr[mid - 1] < target) and arr[mid] == target:
      return mid
    elif arr[mid] < target:
      return self.find_left(arr, target, mid+1, high)
    else:
      return self.find_left(arr, target, low, mid-1)
  
  def find_right(self, arr, target, low, high):
    if low == high and arr[high] != target:
      return -1
    mid = low + (high - low) // 2
    if (mid == len(arr) - 1 or target < arr[mid+1]) and arr[mid] == target:
      return mid
    elif target < arr[mid]:
      return self.find_right(arr, target, low, mid-1)
    else:
      return self.find_right(arr, target, mid+1, high)
  
  def getRange(self, arr, target):
    n = len(arr) - 1
    return [self.find_left(arr, target, 0, n), self.find_right(arr, target, 0, n)]


sol = Solution2()
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(sol.getRange(arr, x))
# [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15] 
x = 9
print(sol.getRange(arr, x))
# [6, 8]

arr = [100, 150, 150, 153] 
x = 150
print(sol.getRange(arr, x))
# [1, 2]

arr = [1, 2, 3, 4]
x = 4
print(sol.getRange(arr, x))
#[3, 3]

arr = [1, 2, 3, 4]
x = 1
print(sol.getRange(arr, x))
#[0, 0]

arr = [1]
x = 1
print(sol.getRange(arr, x))
#[0, 0]

arr = [1,2,3,4,5,6,10] 
x = 9
print(sol.getRange(arr, x))
# [-1, -1]

arr = [1,2,3,4,5,6,10] 
x = 0
print(sol.getRange(arr, x))
# [-1, -1]

arr = [1,2,3,4,5,6,10] 
x = 11
print(sol.getRange(arr, x))
# [-1, -1]
