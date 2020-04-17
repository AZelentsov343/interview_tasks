#Given a string with the initial condition of dominoes, where:

#. represents that the domino is standing still
#L represents that the domino is falling to the left side
#R represents that the domino is falling to the right side

#Figure out the final position of the dominoes. If there are dominoes that
#get pushed on both ends, the force cancels out and that domino remains
#upright.

#Example:
#Input:  ..R...L..R.
#Output: ..RR.LL..RR


class Solution(object): #O(n) time, O(n) memory
  def fall(self, dominoes, left, right, side):
    for i in range(left, right + 1):
      dominoes[i] = side
    
  def pushDominoes(self, dominoes):
    dominoes = list(dominoes)
    loc = []
    for i in range(len(dominoes)):
      if dominoes[i] == 'L':
        loc.append((i, 'L'))
      elif dominoes[i] == 'R':
        loc.append((i, 'R'))
    for loc_i in range(len(loc)):
      i, side = loc[loc_i]
      if side == 'L':
        if loc_i - 1 < 0:
          self.fall(dominoes, 0, i, 'L')
        elif loc[loc_i - 1][1] == 'L':
          self.fall(dominoes, loc[loc_i - 1][0], i, 'L')
        elif loc[loc_i - 1][1] == 'R':
          dist = (i - loc[loc_i - 1][0] - 1) // 2
          self.fall(dominoes, i - dist, i, 'L')
      elif side == 'R':
        if loc_i + 1 >= len(loc):
          self.fall(dominoes, i, len(dominoes) - 1, 'R')
        elif loc[loc_i + 1][1] == 'R':
          self.fall(dominoes, i, loc[loc_i + 1][0], 'R')
        elif loc[loc_i + 1][1] == 'L':
          dist = (loc[loc_i + 1][0] - i - 1) // 2
          self.fall(dominoes, i, i + dist, 'R')
      res = ''
      for c in dominoes:
        res += c
    return res
    

for sol in [Solution()]:
  print(sol.pushDominoes('..R...L..R.'))
  # ..RR.LL..RR
  print()
