#You are given an array of intervals - that is, an array of tuple
#(start, end). The array may not be sorted, and could contain
#overlapping intervals. Return another array where the overlapping
#intervals are merged.

#For example:
#[(1, 3), (5, 8), (4, 10), (20, 25)]

#This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and
#(4, 10) can be merged into (4, 10).


def merge(intervals): #O(n * log(n))
  intervals = sorted(intervals, key = lambda x: x[0]) #O(n * log(n))
  output = []
  ending = None
  for i, interval in enumerate(intervals): #O(n)
    if i == 0 or interval[0] > ending:
      output.append(interval)
      ending = interval[1]
    elif ending < interval[1]:
      output[-1][1] = interval[1]
      ending = interval[1]
  return output 
  
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
