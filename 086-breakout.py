import time
from turtle import Screen
from day86.Paddle import Paddle
from day86.Block import Block, BLOCK_LENGTH
from day86.Ball import Ball
from day86.Scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_ROW = 8
NUM_COL = 9
BLOCK_COLORS = [(255,0,0),(255,128,0),(255,255,0),(0,255,0),(0,255,255),(128,0,255),(255,0,255),(255,0,128)]

window = Screen()
window.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
window.bgcolor("black")
window.title("Breakout")
window.colormode(255)
window.tracer(0)

paddle = Paddle((0, (-SCREEN_HEIGHT / 2) + 20), (128,128,255))
board = []
ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
score = Scoreboard()

window.onkeypress(paddle.left, "a")
window.onkeypress(paddle.right, "d")
window.onkeyrelease(paddle.onKeyUp, "a")
window.onkeyrelease(paddle.onKeyUp, "d")
window.listen()

def countdown(num):  
  # Countdown to game start
  for i in range(num,0,-1):
    score.message(f"{i}")
    time.sleep(1)
  score.message("GO!")
  time.sleep(1)
  score.updateUI()

def resetBoard():
  global board
  board = []
  y = 0
  clrIdx = -1
  for i in range(0, NUM_ROW, 1):
    y += 25
    clrIdx += 1
    x = SCREEN_WIDTH / 2 + 20
    for j in range(0,NUM_COL,1):
      x -= (20 * BLOCK_LENGTH) + 5
      block = Block((x,y), BLOCK_COLORS[clrIdx])
      board.append(block)

def reset():
  ball.resetBall(paddle.getPos())
  resetBoard()
  window.update()
  countdown(3)

def levelUp():
  score.addLevel()
  reset()

def main():
  isAlive = True
  reset()

  while isAlive:
    ball.move()
    paddle.moving()
    
    ball.checkBouncePaddle(*paddle.getBounds())
    # TODO: Change ball angle based on where it hit paddle

    for block in board:
      if(ball.checkBouncePaddle(*block.getBounds())):
        block.reset()
        board.remove(block)
    
    if ball.checkDeathWall():
      reset()
    elif len(board) < 1:
      levelUp()

    window.update()
    time.sleep(.01)
    
  #score.gameOver()
  window.exitonclick()

if __name__ == "__main__":
  main()