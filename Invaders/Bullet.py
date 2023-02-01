from turtle import Turtle, Screen
#from Invaders.GameAssets import PLAYER_SPRITE

PADDING = 40
MOVE_Y = 20

class Bullet(Turtle):
  def __init__(self, pos: tuple[int, int], isUp: bool = False):
    super().__init__(shape="square")
    self.shapesize(stretch_len=.25, stretch_wid=1)
    self.penup()
    self.color("white")
    self.speed("fastest")
    self.goto(pos)
    self.dir = 1 if isUp else -1
  
  def move(self):
    self.goto(self.pos()[0], self.pos()[1] + (MOVE_Y * self.dir))