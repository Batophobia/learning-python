from turtle import Turtle

BLOCK_LENGTH = 4

class Block(Turtle):
  def __init__(self, pos, color=(255,255,255)):
    super().__init__(shape="square")
    self.penup()
    self.shapesize(stretch_len=BLOCK_LENGTH, stretch_wid=1)
    self.color(color)
    self.goto(pos)
    
  def getBounds(self):
    return [
      self.ycor()
      , self.xcor() - (10 * BLOCK_LENGTH)
      , self.xcor() + (10 * BLOCK_LENGTH)
    ]