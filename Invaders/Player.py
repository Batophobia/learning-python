from turtle import Turtle, Screen
from Invaders.GameAssets import PLAYER_SPRITE
from Invaders.BulletManager import BulletManager
from Invaders.Scoreboard import Scoreboard

MOVE_AMOUNT = 20
STARTING_LIVES = 3
FIRE_DELAY = 10

class Player(Turtle):
  def __init__(self, window: Screen, bullets: BulletManager, scoreboard: Scoreboard):
    super().__init__()
    self.penup()
    self.shape(PLAYER_SPRITE)
    self.color("white")
    self.lives = STARTING_LIVES
    self.goto(0, -window.screensize()[1])
    self.bullets = bullets
    self.fireDelay = FIRE_DELAY
    self.canFire = True
    self.scoreboard = scoreboard
    self.respawn()

    window.onkey(self.moveLeft, "Left")
    window.onkey(self.moveRight, "Right")
    window.onkey(self.shoot, "Up")
    window.onkey(self.moveLeft, "a")
    window.onkey(self.moveRight, "d")
    window.onkey(self.shoot, "space")
    window.listen()
  
  def respawn(self):
    self.lives -= 1
    self.scoreboard.lives = self.lives
    if(self.lives <= 0): return False
    return True
  
  def blowUp(self):
    self.respawn()
  
  def tick(self):
    self.fireDelay -= 1
    if self.fireDelay <= 0:
      self.canFire = True
      self.fireDelay = FIRE_DELAY

  def moveLeft(self):
    self.goto(self.pos()[0] - MOVE_AMOUNT, self.pos()[1])
  def moveRight(self):
    self.goto(self.pos()[0] + MOVE_AMOUNT, self.pos()[1])
  def shoot(self):
    if not self.canFire:
      return
    self.canFire = False
    self.bullets.spawn(self.pos(), True)
