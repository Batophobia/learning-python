from turtle import Turtle

LENGTH = 5
MOVE = 20

class Paddle(Turtle):
  def __init__(self, pos, color=(255,255,255)):
    super().__init__(shape="square")
    self.penup()
    self.shapesize(stretch_len=LENGTH, stretch_wid=1)
    self.color(color)
    self.goto(pos)
    self.moving = self.unmoving

  def getBounds(self):
    return [
      self.ycor()
      , self.xcor() - (10 * LENGTH)
      , self.xcor() + (10 * LENGTH)
    ]

  def getPos(self):
    return (
      self.xcor()
      , self.ycor() + 20
    )

  def left(self):
    self.goto(self.xcor() - MOVE, self.ycor())
  def right(self):
    self.goto(self.xcor() + MOVE, self.ycor())
  def unmoving(self):
    pass
    
  def onLeft(self):
    self.moving = self.left
  def onRight(self):
    self.moving = self.right
  def onKeyUp(self):
    self.moving = self.unmoving