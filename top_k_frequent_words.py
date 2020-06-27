#Given a non-empty list of words, return the k most frequent words.
#The output should be sorted from highest to lowest frequency, and if
#two words have the same frequency, the word with lower alphabetical
#order comes first. Input will contain only lower-case letters.

#Example:
#Input: ["daily", "interview", "pro", "pro", 
#"for", "daily", "pro", "problems"], k = 2
#Output: ["pro", "daily"]

import heapq
from collections import defaultdict

class Solution(object):
  def topKFrequent(self, words, k):
    d = defaultdict(int)
    for word in words:
      d[word] += 1
    
    h = []
    for key, val in d.items():
      heapq.heappush(h, (-val, key))
    
    return list(map(lambda x : x[1], heapq.nsmallest(k, h)))
    

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
