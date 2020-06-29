#Given a file path with folder names, '..' (Parent directory), and '.'
#(Current directory), return the shortest possible file path
#(Eliminate all the '..' and '.').

#Example
#Input: '/Users/Joma/Documents/../Desktop/./../'
#Output: '/Users/Joma/'

from functools import reduce

def shortest_path(file_path):
  res = []
  i = 0
  prev = 0
  while i < len(file_path):
    while i < len(file_path) and file_path[i] != '/':
      i += 1
    s = file_path[prev:i+1]
    i += 1
    prev = i
    if s == '../':
      res.pop(len(res) - 1)
    elif s != './':
      res.append(s)
  return reduce(lambda x, y: x + y, res)




print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/
