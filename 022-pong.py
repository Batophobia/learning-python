import time
from turtle import Screen
from Pong.Paddle import Paddle
from Pong.Ball import Ball
from Pong.Scoreboard import Scoreboard

INITIAL_LENGTH = 3
COLLECTION_RANGE = 15
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

window = Screen()
window.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
window.bgcolor("black")
window.title("Pong")
window.colormode(255)
window.tracer(0)

p1 = Paddle(((SCREEN_WIDTH / 2) - 20, 0), (255,0,0))
p2 = Paddle((-(SCREEN_WIDTH / 2) + 20, 0), (64,64,255))
ball = Ball()
score = Scoreboard()

window.onkeypress(p1.up, "Up")
window.onkeypress(p1.down, "Down")
window.onkeypress(p2.up, "w")
window.onkeypress(p2.down, "s")
window.onkeyrelease(p1.onKeUp, "Up")
window.onkeyrelease(p1.onKeUp, "Down")
window.onkeyrelease(p2.onKeUp, "w")
window.onkeyrelease(p2.onKeUp, "s")
window.listen()

def countdown(num):  
  # Countdown to game start
  for i in range(num,0,-1):
    score.message(f"{i}")
    time.sleep(1)
  score.updateUI()


def main():
  window.update()
  isAlive = True

  while isAlive:
    ball.move()
    p1.moving()
    p2.moving()
    
    ball.checkBounceWall(SCREEN_HEIGHT / 2)
    ball.checkBouncePaddle(*p1.getBounds())
    ball.checkBouncePaddle(*p2.getBounds())
    
    if ball.checkScoringWall(SCREEN_WIDTH / 2):
      if ball.xcor() > 0:
        score.addLeft()
      else:
        score.addRight()
      ball.resetBall()

    window.update()
    time.sleep(.01)
    
  #score.gameOver()
  window.exitonclick()

if __name__ == "__main__":
  main()