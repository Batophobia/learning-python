from turtle import Turtle
from random import randint
import time

SIZE = 10
MOVE = 5

class Ball(Turtle):
  def __init__(self, maxX, maxY):
    super().__init__(shape="circle")
    self.penup()
    self.shapesize(stretch_len=SIZE / 20, stretch_wid=SIZE / 20)
    self.color("white")
    self.maxX = maxX
    self.maxY = maxY
    self.resetBall()

  def resetBall(self, pos=(0, 0)):
    self.goto(pos)
    self.setheading(0)
    self.left(randint(45,135))

  def move(self):
    self.forward(MOVE)
    self.checkBounceWall()

  def checkDeathWall(self):
    if self.ycor() <= -self.maxY + SIZE:
      return True
    return False

  def checkBounceWall(self):
    if self.xcor() >= self.maxX - SIZE or self.xcor() <= -self.maxX + SIZE:
      self.setheading(180 - self.heading())
    if self.ycor() >= self.maxY - SIZE:
      self.setheading(-self.heading())

  def checkBouncePaddle(self, yPos, xMin, xMax):
    if self.ycor() >= yPos - SIZE and self.ycor() <= yPos + SIZE:
      if self.xcor() >= xMin and self.xcor() <= xMax:
        self.setheading(-self.heading())
        return True
    return False