#You are given a 2D array of integers. Print out the clockwise spiral
#traversal of the matrix.

#Example:

#grid = [[1,  2,  3,  4,  5],
#        [6,  7,  8,  9,  10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20]]

#The clockwise spiral traversal of this array is:

#1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12


def matrix_spiral_print(M): # O(n * m) time (cant do faster) O(1) memory
  end_row = len(M)
  if end_row == 0:
    return
  end_col = len(M[0])
  start_col = 0
  start_row = 0
  while start_row < end_row and start_col < end_col:
    for i in range(start_col, end_col):
      print(M[start_row][i], end=' ') #print first col
    start_row += 1
    
    if start_row >= end_row: break
    for i in range(start_row, end_row):
      print(M[i][end_col - 1], end=' ')
    end_col -= 1

    if start_col >= end_col: break
    for i in range(end_col - 1, start_col - 1, -1):
      print(M[end_row - 1][i], end=' ')
    end_row -= 1

    if start_row >= end_row: break
    for i in range(end_row - 1, start_row - 1, -1):
      print(M[i][start_col], end=' ')
    start_col += 1

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
print()

grid = [[1, 2],
        [4, 3]]
matrix_spiral_print(grid)
# 1 2 3 4
print()

grid = [[1]]
matrix_spiral_print(grid)
# 1
print()

grid = [[]]
matrix_spiral_print(grid)
#
print()
grid = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]

matrix_spiral_print(grid)
print()
# 1 2 3 4 8 12 11 10 9 5 6 7
