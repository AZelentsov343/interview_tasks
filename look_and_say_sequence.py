# A look-and-say sequence is defined as the integer sequence beginning with a single digit in which
#the next term is obtained by describing the previous term. An example is easier to understand:

#Each consecutive value describes the prior value.

#1      #
#11     # one 1's
#21     # two 1's
#1211   # one 2, and one 1.
#111221 # #one 1, one 2, and two 1's.

#1 -> one 1 -> 11
#11 -> two 1 -> 21
#21 -> one 2 one 1 -> 1211
#1211 -> one 1 one 2 two 1 -> 111221
#111221 -> three 1 two 2 one 1 -> 312211

#Your task is, return the nth term of this sequence.


def next_seq(a):
  prev = a[0]
  res = ''
  l = 1
  for i in range(1, len(a)):
    if a[i] != prev:
      res += str(l) + prev
      l = 1
      prev = a[i]
    else:
      l += 1
  res += str(l)
  res += prev
  return res


def count_and_say(n):
  a = '1'
  for _ in range(n - 1):
    a = next_seq(a)
  return a
    

# Testing
for i in range(10):
  print(count_and_say(i))
