from turtle import Turtle

LENGTH = 5
MOVE = 20

class Paddle(Turtle):
  def __init__(self, pos, color=(255,255,255)):
    super().__init__(shape="square")
    self.penup()
    self.shapesize(stretch_len=1, stretch_wid=LENGTH)
    self.color(color)
    self.goto(pos)
    self.moving = self.unmoving

  def getBounds(self):
    return [
      self.xcor()
      , self.ycor() - (10 * LENGTH)
      , self.ycor() + (10 * LENGTH)
    ]

  def up(self):
    self.goto(self.xcor(), self.ycor() + MOVE)
  def down(self):
    self.goto(self.xcor(), self.ycor() - MOVE)
  def unmoving(self):
    pass
    
  def onUp(self):
    self.moving = self.up
  def onDown(self):
    self.moving = self.up
  def onKeUp(self):
    self.moving = self.unmoving