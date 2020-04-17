# Given two strings, determine the edit distance between them. The edit
#distance is defined as the minimum number of edits (insertion, deletion, or
#substitution) needed to change one string to the other.

#For example, "biting" and "sitting" have an edit distance of 2 (substitute
#b for s, and insert a t).

def distance1(s1, s2): #O(3^m) time + recursive memory
  n = len(s1)
  m = len(s2)
  if n == 0:
    return m
  if m == 0:
    return n
  if s1[n - 1] == s2[m - 1]:
    return distance1(s1[:n-1], s2[:m-1])
  return 1 + min(distance1(s1[:n-1], s2), #remove
                 distance1(s1, s2[:m-1]), #insert
                 distance1(s1[:n-1], s2[:m-1])) #replace

def distance2(s1, s2): #O(n * m) time O(n * m) memory
  n = len(s1)
  m = len(s2)
  distances = [[0 for j in range(m + 1)] for i in range(n + 1)]
  for i in range(n + 1):
    for j in range(m + 1):
      if i == 0:
        distances[i][j] = j
      elif j == 0:
        distances[i][j] = i
      elif s1[i - 1] == s2[j - 1]:
        distances[i][j] = distances[i - 1][j - 1]
      else:
        distances[i][j] = 1 + min(distances[i - 1][j], #remove
                                  distances[i][j - 1], #insert
                                  distances[i - 1][j - 1]) # replace
  return distances[n][m]

def distance3(s1, s2): #O(n * m) time O(m) memory cause we can store only 2
  n = len(s1)
  m = len(s2)
  
  if n == 0:
    return m
  
  if m == 0:
    return n

  distances = [[j, 0] for j in range(m + 1)]

  for i in range(1, n + 1):
    for j in range(m + 1):
      if j == 0:
        distances[j][i % 2] = i
      elif s1[i - 1] == s2[j - 1]:
        distances[j][i % 2] = distances[j - 1][(i - 1) % 2]
      else:
        distances[j][i % 2] = 1 + min(distances[j][(i - 1)%2], #remove
                                      distances[j - 1][i % 2], #insert
                                  distances[j - 1][(i - 1) % 2]) # replace
  return distances[m][n % 2]


# Testing
for distance in [distance1, distance2, distance3]:
  print(distance('biting', 'sitting'))
  # 2
  print(distance('saturday', 'sunday'))
  # 3
  print(distance('abc', 'xyz'))
  # 3
  print(distance('food', 'money'))
  # 4
  print()
