#Version numbers are strings that are used to identify unique states
#of software products. A version number is in the format a.b.c.d. and
#so on where a, b, etc. are numeric strings separated by dots. These
#generally represent a hierarchy from major to minor changes. Given
#two version numbers version1 and version2, conclude which is the
#latest version number. Your code should do the following: 
#If version1 > version2 return 1. 
#If version1 < version2 return -1.
#Otherwise return 0. 

#Note that the numeric strings such as a, b, c, d, etc. may have
#leading zeroes, and that the version strings do not start or end with
#dots. Unspecified level revision numbers default to 0.

#Example:
#Input: 
#version1 = "1.0.33"
#version2 = "1.0.27"
#Output: 1 
#version1 > version2

#Input:
#version1 = "0.1"
#version2 = "1.1"
#Output: -1
#version1 < version2

#Input: 
#version1 = "1.01"
#version2 = "1.001"
#Output: 0
#ignore leading zeroes, 01 and 001 represent the same number. 

#Input:
#version1 = "1.0"
#version2 = "1.0.0"
#Output: 0
#version1 does not have a 3rd level revision number, which
#defaults to "0"


class Solution:
  def compareVersion(self, version1, version2):
    s1 = list(map(int, version1.split('.')))
    s2 = list(map(int, version2.split('.')))
    c1, c2 = 0, 0
    for i in range(max(len(s1), len(s2))):
      c1 = s1[i] if i < len(s1) else 0
      c2 = s2[i] if i < len(s2) else 0
      if c1 < c2:
        return -1
      elif c1 > c2:
        return 1
    return 0

version1 = "1.0.1"
version2 = "1"
print(Solution().compareVersion(version1, version2))
# 1
