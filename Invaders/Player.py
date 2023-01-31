from turtle import Turtle

MOVE_AMOUNT = 20
STARTING_LIVES = 3

class Player(Turtle):
  def __init__(self, window):
    super().__init__(shape="circle")
    self.penup()
    self.shapesize(stretch_len=6, stretch_wid=2)
    self.color("white")
    self.window = window
    self.lives = STARTING_LIVES
    self.respawn()

    window.onkey(self.moveLeft, "Left")
    window.onkey(self.moveRight, "Right")
    window.listen()
  
  def respawn(self):
    self.lives -= 1
    if(self.lives <= 0): return False
    return True

  def moveLeft(self):
    self.goto(self.pos[0] - MOVE_AMOUNT,self.pos[1])
  def moveRight(self):
    self.goto(self.pos[0] + MOVE_AMOUNT, self.pos[1])
