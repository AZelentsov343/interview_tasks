#Given a list of string formatted like '{substring}_{number}.{something}'
#Sort them descending by {substring} and ascending by {number}

l = ['example_1.txt', 'example_2.tar', 'abc_1.py']

class Solution:
  def sort(self, l):
    return sorted(l, key=lambda s: (s.split('_')[0], -int(s.split('_')[1].split('.')[0])))

print(Solution().sort(l))
