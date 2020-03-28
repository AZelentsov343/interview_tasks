#Given a list of words
#After that one word is given
#If word is in list of words ---> return (True, [])
#If word isn't in list of words ---> return (False,
#                                       [{all words from list, that can be generated by inserting one char in a given word}])
# After one word is given, must work not slower than O(len(word))
words = ['cat', 'rat', 'bart', 'build', 'play']

from collections import defaultdict


class Solution:
  def __init__(self, words):
    self.typos = defaultdict(list)
    self.corrects = set(words)
    for word in words:
      for i in range(len(word)):
        typo = word[:i] + word[i+1:]
        self.typos[typo].append(word)

  def find(self, word):
    if word in self.corrects:
      return True, []
    else:
      return False, self.typos[word]


#Test
sol = Solution(words)

print(sol.find('cat'))
# True, []
print(sol.find('at'))
# False, ['cat', 'rat']
print(sol.find('buld'))
# False, ['build']
print(sol.find('gvuyvuy'))
# False, []
