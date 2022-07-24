
board = [
  [" ", " ", " "],
  [" ", " ", " "],
  [" ", " ", " "],
]

def printboard(board):
  print("---------------")
  for row in board:
    for char in row:
      print("|", char, end = " |")
    print(" ")
    print("---------------")

for row in range(9):
  row1 = int(input("Pick a row: "))
  print(row1)
  char1 = int(input("Pick a column: "))
  print(char1)
  board[row1][char1] = "x"
  printboard(board)
  row1 = int(input("Pick a row: "))
  print(row1)
  char1 = int(input("Pick a column: "))
  print(char1)
  board[row1][char1] = "o"
  printboard(board)
    
