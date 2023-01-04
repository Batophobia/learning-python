from turtle import Turtle

STARTING_POSITION = (0, -270)

class Player(Turtle):
  def __init__(self, gridSize, yMax):
    super().__init__()
    self.color("green")
    self.shape("turtle")
    self.penup()
    self.shapesize(stretch_len=.75, stretch_wid=.75)
    self.moveDistance = gridSize
    self.finishLine = yMax
    self.reset()
  
  def finished(self):
    if self.ycor() >= self.finishLine:
      return True
    return False

  def reset(self):
    self.goto(STARTING_POSITION)
    self.setheading(90)

  def move(self):
    self.forward(self.moveDistance)

  def moveUp(self):
    self.setheading(90)
    self.move()
  def moveLeft(self):
    self.setheading(180)
    self.move()
  def moveRight(self):
    self.setheading(0)
    self.move()
  def moveDown(self):
    self.setheading(270)
    self.move()