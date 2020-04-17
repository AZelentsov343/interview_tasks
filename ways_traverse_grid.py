#You 2 integers n and m representing an n by m grid, determine the
#number of ways you can get from the top-left to the bottom-right of
#the matrix y going only right or down.

#Example:
#n = 2, m = 2

#This should return 2, since the only possible routes are:
#Right, down
#Down, right.

def num_ways1(n, m): # (2 ^ (n * m)) recursive way
  if n == 1 and m == 1:
    return 1
  elif n == 1:
    return num_ways1(n, m - 1)
  elif m == 1:
    return num_ways1(n - 1, m)
  else:
    return num_ways1(n - 1, m) + num_ways1(n, m - 1)

def num_ways2(n, m): # O(n * m) time, O(n * m) memory
  num_w = [[0 for j in range(m)] for i in range(n)]
  num_w[0][0] = 1
  for i in range(n):
    for j in range(m):
      if i == 0 and j == 0:
        continue
      elif i == 0:
        num_w[i][j] = num_w[i][j - 1]
      elif j == 0:
        num_w[i][j] = num_w[i - 1][j]
      else:
        num_w[i][j] = num_w[i - 1][j] + num_w[i][j - 1]
  return num_w[n - 1][m - 1]

def num_ways3(n, m): #O(n * m) time, O(min(n, m)) memory
  if m > n:
    m, n = n, m
  num_w = [[0 for j in range(m)] for i in range(2)]
  num_w[0][0] = 1
  for i in range(n):
    for j in range(m):
      if i == 0 and j == 0:
        continue
      elif i == 0:
        num_w[i % 2][j] = num_w[i % 2][j - 1]
      elif j == 0:
        num_w[i % 2][j] = num_w[(i - 1) % 2][j]
      else:
        num_w[i % 2][j] = num_w[(i - 1) % 2][j] + num_w[i % 2][j - 1]
  return num_w[(n - 1) % 2][m - 1]


for num_ways in [num_ways1, num_ways2, num_ways3]:
  print(num_ways(2, 2))
  # 2
  print()
