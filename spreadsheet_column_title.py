#MS Excel column titles have the following pattern: A, B, C, ..., Z,
#AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc. In other words,
#column 1 is named "A", column 2 is "B", column 26 is "Z", column 27
#is "AA" and so forth. Given a positive integer, find its
#corresponding column name. 

#Examples:
#Input: 26
#Output: Z

#Input: 51
#Output: AY

#Input: 52
#Output: AZ

#Input: 676
#Output: YZ

#Input: 702
#Output: ZZ

#Input: 704
#Output: AAB


class Solution: # O(log_26(N)) time
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z']
  def convertToTitle(self, n):
    ans = ''
    while n > 0:
      n -= 1
      ans += self.letters[n % 26]
      n //= 26
    return ans[::-1]
    

input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB
