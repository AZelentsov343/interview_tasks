#Given a list of words, and an arbitrary alphabetical order, verify
#that the words are in order of the alphabetical order.

#Example:
#Input:
#words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

#Output: False
#Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

#Example 2:
#Input:
#words = ["zyx", "zyxw", "zyxwy"],
#order="zyxwvutsrqponmlkjihgfedcba"

#Output: True
#Explanation: The words are in increasing alphabetical order

def words_in_order(word1, word2, order):
  i = 0
  while i < len(word1) and i < len(word2):
    if order.index(word1[i]) > order.index(word2[i]):
      return False
    i += 1
  if i < len(word1):
    return False
  return True
    

def isSorted(words, order):
  for i in range(len(words) - 1):
    if not words_in_order(words[i], words[i+1], order):
      return False
  return True

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True
