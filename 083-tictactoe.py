from tools import getOneOfThese
from day83.Board import Board

def main():
  runAgain = True
  while runAgain:
    board = Board()
    winner = ""
    while(winner == ""):
      board.drawBoard()
      move = getOneOfThese(f"It is {board.getTurn()}'s turn.  Select an open space: ", board.openSpots())
      board.takeSpace(int(move))
      winner = board.checkWin()
    board.drawBoard()
    if input(f"{winner} has won.  Play again (Y/n)? ").lower() != "y":
      runAgain = False

if __name__ == "__main__":
  main()