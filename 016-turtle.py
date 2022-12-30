import turtle
import random

def changeColor(turt, red: int, green: int, blue: int):
  turt.color(red, green, blue)

def penColor(turt, red: int, green: int, blue: int):
  turt.pencolor(red, green, blue)

def moveTurtle(turt, distance: int):
  turt.forward(distance)

TURN_AMOUNT = 30
def turnLeft():
  donny.left(TURN_AMOUNT)
def turnRight():
  donny.right(TURN_AMOUNT)

def init():
  turt = turtle.Turtle()
  turt.shape("turtle")
  turt.home()
  return turt

donny = init()
def main():
  window = turtle.Screen()
  window.onkey(turnLeft, "Left")
  window.onkey(turnRight, "Right")
  window.colormode(255)
  window.listen()
  
  changeColor(donny, 0, 90, 0)
  
  for i in range(100):
    moveTurtle(donny, random.randint(10,20))
    penColor(donny, random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if random.randint(0,10) < 5:
      turnLeft()
    else:
      turnRight()
  
  window.exitonclick()

if __name__ == "__main__":
  main()