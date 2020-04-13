#You are given a 2D array of characters, and a target string. Return whether or not
#the word target word exists in the matrix. Unlike a standard word search, the word
#must be either going left-to-right, or top-to-bottom in the matrix.

#Example:

#[['F', 'A', 'C', 'I'],
# ['O', 'B', 'Q', 'P'],
# ['A', 'N', 'O', 'B'],
# ['M', 'A', 'S', 'S']]

# Given this matrix, and the target word FOAM, you should return true, as it can be
# found going up-to-down in the first column.

def word_search(matrix, word): # O(max(len(word), n * m)) time O(n * m) memory
  if len(word) == 0:
    return True
  start_pos = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == word[0]:
        start_pos.append((i, j))
  if len(word) == 1:
    return len(start_pos) != 0
  movements = []
  pos = 1
  for i, j in start_pos:
    if matrix[i + 1][j] == word[pos]:
      movements.append((i + 1, j, 'bottom'))
    if matrix[i][j + 1] == word[pos]:
      movements.append((i, j + 1, 'right'))
  for pos in range(2, len(word)):
    new_arr = []
    for i, j, where in movements:
      if where == 'bottom' and matrix[i + 1][j] == word[pos]:
        new_arr.append((i + 1, j, 'bottom'))
      elif where == 'right' and matrix[i][j + 1] == word[pos]:
        new_arr.append((i, j + 1, 'right'))
    movements = new_arr
  return len(movements) != 0


matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))
# True
