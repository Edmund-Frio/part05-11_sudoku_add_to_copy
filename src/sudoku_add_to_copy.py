def print_sudoku(sudoku: list):
  for i in range(len(sudoku)):
    if i > 0 and i % 3 == 0:
      print()
    for j in range(len(sudoku[i])):
      if j > 0 and j % 3 == 0:
        print(" ", end="")
      value = sudoku[i][j]
      if value == 0:
        print("_", end=" ")
      else:
        print(value, end=" ")
    print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
  sudoku_copy = []
  for row in sudoku:
    sudoku_copy.append(row[:])
  sudoku_copy[row_no][column_no] = number
    
  return sudoku_copy
  
  
if __name__ == "__main__":
  sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]

  grid_copy = copy_and_add(sudoku, 0, 0, 2)
  print("Original:")
  print_sudoku(sudoku)
  print()
  print("Copy:")
  print_sudoku(grid_copy)
  