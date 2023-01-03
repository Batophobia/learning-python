from turtle import Turtle
from random import randint
import time

SIZE = 10
MOVE = 5

class Ball(Turtle):
  def __init__(self):
    super().__init__(shape="circle")
    self.penup()
    self.shapesize(stretch_len=SIZE / 20, stretch_wid=SIZE / 20)
    self.color("white")
    self.resetBall()

  def resetBall(self):
    self.goto(0,0)
    self.setheading(0)
    self.left(randint(135,225))
    temp = randint(0, 10)
    if(temp < 5):
      self.setheading(self.heading() - 180)

  def move(self):
    self.forward(MOVE)

  def checkScoringWall(self, maxX):
    if self.xcor() >= maxX - SIZE or self.xcor() <= -maxX + SIZE:
      return True
    return False

  def checkBounceWall(self, maxY):
    if self.ycor() >= maxY - SIZE or self.ycor() <= -maxY + SIZE:
      self.setheading(-self.heading())

  def checkBouncePaddle(self, xPos, yMin, yMax):
    if self.xcor() >= xPos - SIZE and self.xcor() <= xPos + SIZE:
      if self.ycor() >= yMin and self.ycor() <= yMax:
        self.setheading(180 - self.heading())