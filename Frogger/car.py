from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):    
  def __init__(self, pos, color, moveLeft = True):
    super().__init__()
    self.shape("square")
    self.shapesize(stretch_len=2, stretch_wid=1.25)
    self.penup()
    self.color(color)
    self.goto(pos)
    self.awaitingDelete = False
    if moveLeft:
      self.left(180)
  
  def move(self, maxX):
    self.forward(MOVE_INCREMENT)
    if self.xcor() >= maxX + 50 or self.xcor() <= -maxX - 50:
      if self.awaitingDelete:
        self.delete()
        return True
      else:
        self.goto(-self.xcor(), self.ycor())
    return False
      
  def delete(self):
    self.shape("blank")

  def markForPop(self):
    self.awaitingDelete = True

  def checkSquish(self, pos, gridSize):
    if self.xcor() - 40 <= pos[0] and self.xcor() + 40 >= pos[0]:
      if self.ycor() - 25 <= pos[1] and self.ycor() + 25 >= pos[1]:
        return True
    return False