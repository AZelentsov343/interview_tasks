#You are given a string s, and an integer k. Return the length of the
#longest substring in s that contains at most k distinct characters.

#For instance, given the string:
#aabcdefff and k = 3, then the longest substring with 3 distinct
#characters would be defff. The answer should be 5.

#Here's a starting point:

from collections import defaultdict

def longest_substring_with_k_distinct_characters(s, k):
  counts = defaultdict(int)
  cur_max_length = 0
  begin = 0
  end = 0
  while end <= len(s) - 1:
    while end != len(s) - 1 and len(counts) <= k:
      counts[s[end]] += 1
      end += 1
    if end - begin + 1 > cur_max_length and len(counts) == k:
      cur_max_length = end - begin + 1
    if end == len(s) - 1:
      break
    while begin != end and len(counts) > k:
      counts[s[begin]] -= 1
      if counts[s[begin]] == 0:
        del counts[s[begin]]
      begin += 1
  return cur_max_length
      

print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
