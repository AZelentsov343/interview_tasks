#You are given an array of integers in an arbitrary order. Return
#whether or not it is possible to make the array non-decreasing by
#modifying at most 1 element to any value.

#We define an array is non-decreasing if array[i] <= array[i + 1]
#holds for every i (1 <= i < n).

#Example:

#[13, 4, 7] should return true, since we can modify 13 to any value 4
#or less, to make it non-decreasing.

#[13, 4, 1] however, should return false, since there is no way to
#modify just one element to make the array non-decreasing.

# Can you find a solution in O(n) time?

def check(lst): # O(n) time
  mod_made = False
  n = len(lst)
  if n <= 2:
    return True
  if (lst[0] > lst[1]):
    lst[0] = lst[1] - 1
    mod_made = True
  for i in range(1, n - 1):
    if (lst[i] > lst[i+1] and lst[i] > lst[i-1]) or (lst[i] <= lst[i+1] and lst[i] <= lst[i-1]):
      if mod_made:
        return False
      lst[i] = (lst[i-1] + lst[i+1])/2
      mod_made = True
  if mod_made and (lst[n-2] > lst[n-1]):
    return False
  return True

#Testing
print(check([13, 4, 7]))
# True
print(check([1, 2, 3, 4, 5]))
# True
print(check([1, 3, 2, 4, 5]))
# True
print(check([8, 2, 3, 4, 5]))
# True
print(check([4]))
# True
print(check([2, 1]))
# True
print(check([8, 1, 2, 3, 0]))
# False
print(check([3, 2, 1]))
# False
print(check([1, 4, 3, 2, 5]))
# False
print(check([5,1,3,2,5]))
# False
print(check([1, 2, 3, 4, 0]))
# False
