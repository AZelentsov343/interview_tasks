#An IP Address is in the format of A.B.C.D, where A, B, C, D are all
#integers between 0 to 255.

#Given a string of numbers, return the possible IP addresses you can
#make with that string by splitting into 4 parts of A, B, C, D.

#Keep in mind that integers can't start with a 0! (Except for 0)

#Example:
#Input: 1592551013
#Output: ['159.255.101.3', '159.255.10.13']
def ip_addresses(s, ip_parts=[]):
  ans = []
  for first in range(1, 4):
    if len(s) - first > 9: continue
    if len(s) - first < 3: break 
    if s[0] == '0' and first > 1: break
    if int(s[:first]) > 255: break
    for second in range(first + 1, first + 4):
      if len(s) - second > 6: continue
      if len(s) - second < 2: break
      if s[first] == '0' and second - first > 1: break
      if int(s[first:second]) > 255: break
      for third in range(second + 1, second + 4):
        if (len(s) - third) > 3:continue
        if s[third] == '0' and third != len(s) - 1: continue
        if len(s) - third < 1: break
        if s[second] == '0' and third - second > 1: break
        if int(s[second:third]) > 255: break
        ans.append(s[:first]+'.'+s[first:second]+'.'+s[second:third]+'.'+s[third:])
  return ans




print(ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']
