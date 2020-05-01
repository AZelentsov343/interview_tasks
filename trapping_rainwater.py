#Hi, here's your problem today. This problem was recently asked by Uber:

#You have a landscape, in which puddles can form. You are given an
#array of non-negative integers representing the elevation at each
#location. Return the amount of water that would accumulate if it
#rains.

#For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6
#units of water can get trapped here.
#       X               
#   X███XX█X              
# X█XX█XXXXXX                   
# [0,1,0,2,1,0,1,3,2,1,2,1]


def capacity(arr): #O(n) time O(1) memory
  result = 0
  left_max = 0
  right_max = 0
       
  left = 0
  right = len(arr) - 1
       
  while(left <= right):  
    if arr[left] < arr[right]: 
      if arr[left] > left_max: 
        left_max = arr[left] 
      else:
        result += left_max - arr[left] 
      left += 1
    else: 
      if arr[right] > right_max: 
        right_max = arr[right] 
      else: 
        result += right_max - arr[right] 
      right -= 1
  return result 

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
