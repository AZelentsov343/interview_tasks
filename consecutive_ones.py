#Return the longest run of 1s for a given integer n's binary
#representation.

#Example:
#Input: 242
#Output: 4
#242 in binary is 0b11110010, so the longest run of 1 is 4.

def longest_run(n):
  res = 0
  cur = 0
  for i in range(32):
    if n & (1 << i) != 0:
      cur += 1
    else:
      res = cur if cur > res else res
      cur = 0
  res = cur if cur > res else res
  return res
    
print(longest_run(242))
# 4
