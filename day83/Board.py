from tools import isNumber, cls

class Board():
  board = ["1","2","3","4","5","6","7","8","9"]
  turn = "X"
  def __init__(self):
    self.board = ["1","2","3","4","5","6","7","8","9"]
    self.turn = "X"

  def takeSpace(self,idx):
    idx = idx - 1
    if(not isNumber(self.board[idx])):
      return
    self.board[idx] = self.turn
    self.turn = "X" if self.turn == "O" else "O" # ternary

  def getTurn(self):
    return self.turn

  # 1 | 2 | 3
  #---+---+---
  # 4 | 5 | 6
  #---+---+---
  # 7 | 8 | 9
  def drawBoard(self):
    cls()
    ui = "+---+---+---+\n"
    for i in range(len(self.board)):
      ui += f"| {self.board[i]} "
      if(i % 3 == 2):
        ui += "|\n+---+---+---+\n"
    print(ui)
  
  def openSpots(self):
    return [v for v in self.board if v != "X" and v != "O"] # filter

  def checkWin(self):
    winner = ""
    ### ROWS ###
    if((not isNumber(self.board[0])) and self.board[0] == self.board[1] and self.board[0] == self.board[2]): # Row 1
      winner = self.board[0]
    elif((not isNumber(self.board[3])) and self.board[3] == self.board[4] and self.board[3] == self.board[5]): # Row 2
      winner = self.board[3]
    elif((not isNumber(self.board[6])) and self.board[6] == self.board[7] and self.board[6] == self.board[8]): # Row 3
      winner = self.board[6]
    ### COLUMNS ###
    if((not isNumber(self.board[0])) and self.board[0] == self.board[3] and self.board[0] == self.board[6]): # Col 1
      winner = self.board[0]
    elif((not isNumber(self.board[1])) and self.board[1] == self.board[4] and self.board[1] == self.board[7]): # Col 2
      winner = self.board[1]
    elif((not isNumber(self.board[2])) and self.board[2] == self.board[5] and self.board[2] == self.board[8]): # Col 3
      winner = self.board[2]
    ### DIAGONALS ###
    if((not isNumber(self.board[0])) and self.board[0] == self.board[4] and self.board[0] == self.board[8]): # Diag 1
      winner = self.board[0]
    elif((not isNumber(self.board[2])) and self.board[2] == self.board[4] and self.board[2] == self.board[6]): # Diag 2
      winner = self.board[2]

    return winner