import turtle
import random

def changeColor(turt, red: int, green: int, blue: int):
  turt.color(red, green, blue)

def moveTurtle(turt, distance: int):
  turt.forward(distance)

TURN_AMOUNT = 15
def turnLeft(turt, amount = TURN_AMOUNT):
  turt.left(amount)
def turnRight(turt, amount = TURN_AMOUNT):
  turt.right(amount)

def init(turt, x=0, y=0):
  turt.shape("turtle")
  turt.pensize(5)
  turt.penup()
  turt.goto(x, y)
  turt.pendown()

def winner(turts, goal: int):
  for t in turts:
    if t.xcor() >= goal:
      return t
  return False

def victoryDance(turt):
  turt.penup()
  turt.goto(turt.xcor(), 0)
  turt.pendown()
  turnLeft(turt, 90)
  for i in range(25):
    moveTurtle(turt, MAX_MOVE - i)
    turnLeft(turt)
    moveTurtle(turt, MAX_MOVE - i)
    turnRight(turt)
    moveTurtle(turt, MAX_MOVE - i)
    turnLeft(turt)

MIN_MOVE = 5
MAX_MOVE = 30

donny = turtle.Turtle()
mikey = turtle.Turtle()
leo = turtle.Turtle()
raph = turtle.Turtle()
franklin = turtle.Turtle()
turtonator = turtle.Turtle()
turts = [raph, mikey, turtonator, franklin, leo, donny]

def main():
  window = turtle.Screen()
  #window.onkey(turnLeft, "Left")
  #window.onkey(turnRight, "Right")
  window.colormode(255)
  window.listen()

  firstPos = window.canvheight
  for t in turts:
    init(t, -window.canvwidth, firstPos)
    firstPos -= window.canvheight/len(turts) * 2
  
  changeColor(donny, 125, 0, 255)
  changeColor(mikey, 255, 125, 0)
  changeColor(leo, 0, 0, 255)
  changeColor(raph, 255, 0, 0)
  changeColor(franklin, 0, 255, 0)
  changeColor(turtonator, 255, 255, 0)
  
  hasWinner = False
  while not hasWinner:
    for t in turts:
      moveTurtle(t, random.randint(MIN_MOVE,MAX_MOVE))
    hasWinner = winner(turts, window.canvwidth)
  victoryDance(hasWinner)

  window.exitonclick()

if __name__ == "__main__":
  main()