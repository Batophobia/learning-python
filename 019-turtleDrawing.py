import turtle
import random

leo = turtle.Turtle()
window = turtle.Screen()

FORWARD_AMOUNT = 10
def moveForward():
  leo.forward(FORWARD_AMOUNT)

TURN_AMOUNT = 15
def turnLeft():
  leo.left(TURN_AMOUNT)
def turnRight():
  leo.right(TURN_AMOUNT)

MIN_SIZE = 1
CUR_SIZE = 1
MAX_SIZE = 50
def increaseSize():
  global CUR_SIZE
  CUR_SIZE += 1
  if(CUR_SIZE > MAX_SIZE):
    CUR_SIZE = MAX_SIZE
  leo.pensize(CUR_SIZE)
def decreaseSize():
  global CUR_SIZE
  CUR_SIZE -= 1
  if(CUR_SIZE < MIN_SIZE):
    CUR_SIZE = MIN_SIZE
  leo.pensize(CUR_SIZE)

MIN_FORWARD_AMOUNT = 30
MAX_FORWARD_AMOUNT = 500
FORWARD_AMOUNT_CHANGE = 10
def increaseSpeed():
  global FORWARD_AMOUNT
  FORWARD_AMOUNT += FORWARD_AMOUNT_CHANGE
  if(FORWARD_AMOUNT > MAX_FORWARD_AMOUNT):
    FORWARD_AMOUNT = MAX_FORWARD_AMOUNT
def decreaseSpeed():
  global FORWARD_AMOUNT
  FORWARD_AMOUNT -= FORWARD_AMOUNT_CHANGE
  if(FORWARD_AMOUNT < MIN_FORWARD_AMOUNT):
    FORWARD_AMOUNT = MIN_FORWARD_AMOUNT

def clearScreen():
  leo.clear()

#          BLACK     RED      ORANGE      YELLOW        LIME      GREEN       TEAL        CYAN        BLUE      NAVY      PURPLE        PINK      MAGENTA
COLORS = [(0,0,0),(255,0,0),(255,128,0),(255,255,0),(128,255,0),(0,255,0),(0,255,128),(0,255,255),(0,128,255),(0,0,255),(128,0,255),(255,0,255),(255,0,128)]
colorIdx = 0
def changeColor():
  global colorIdx
  colorIdx = (colorIdx + 1) % len(COLORS)
  leo.pencolor(COLORS[colorIdx])
  

def main():
  leo.shape("classic")
  window.colormode(255)
  window.onkey(moveForward, "Up")
  window.onkey(turnLeft, "Left")
  window.onkey(turnRight, "Right")
  window.onkey(increaseSize, "+")
  window.onkey(decreaseSize, "-")
  window.onkey(increaseSpeed, "f")
  window.onkey(decreaseSpeed, "s")
  window.onkey(clearScreen, "BackSpace")
  window.onkey(changeColor, "c")
  window.listen()

  window.exitonclick()

if __name__ == "__main__":
  main()