from turtle import Turtle, Screen
from Invaders.Bullet import Bullet

HIT_PADDING_X = 40
HIT_PADDING_Y = 35

class BulletManager(Turtle):
  def __init__(self, gameSize: tuple[int, int]):
    super().__init__()
    self.penup()
    self.gameSize = gameSize
    self.bullets = []
  
  def spawn(self, pos: tuple[int, int], isUp: bool):
    bullet = Bullet(pos, isUp)
    self.bullets.append(bullet)

  def move(self):
    for bullet in self.bullets:
      bullet.move()
      if(abs(bullet.pos()[1]) > self.gameSize[1]):
        bullet.reset()
        self.bullets.remove(bullet)
  
  def check(self, entity: Turtle):
    for bullet in self.bullets:
      if(
        bullet.pos()[1] < entity.pos()[1] + HIT_PADDING_Y and
        bullet.pos()[1] > entity.pos()[1] - HIT_PADDING_Y and
        bullet.pos()[0] > entity.pos()[0] - HIT_PADDING_X and
        bullet.pos()[0] < entity.pos()[0] + HIT_PADDING_X
      ):
        if(
          (type(entity).__name__ == 'Enemy' and bullet.dir > 0) or
          (type(entity).__name__ == 'Player' and bullet.dir < 0)
        ):
          entity.blowUp()
          bullet.reset()
          self.bullets.remove(bullet)