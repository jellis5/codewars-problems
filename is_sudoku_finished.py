#From http://www.codewars.com/kata/53db96041f1a7d32dc0004d2

#Description:

#Write a function done_or_not passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

#Sudoku rules:

#Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

#Rows:

#There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

#Columns:

#There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

#Regions:

#A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

#Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

def done_or_not(board):
  nums = set(range(1, 10))
  # check rows
  for row in board:
      row = set(row)
      if row != nums:
          return 'Try again!'
  # check columns
  for i in range(9):
      column = set()
      for row in board:
          column.add(row[i])
      if column != nums:
          return 'Try again!'
  # check boxes
  start, end = 0, 3
  while end <= 9:
      box = set()
      for iRow in range(start, end):
          for iColumn in range(start, end):
              box.add(board[iRow][iColumn])
      if box != nums:
          return 'Try again!'
      start += 3
      end += 3
  return 'Finished!'
