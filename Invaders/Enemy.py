from turtle import Turtle
from Invaders.GameAssets import EXPLODE_SPRITE
from Invaders.Scoreboard import Scoreboard

MOVE_X = 10
MOVE_Y = 20

class Enemy(Turtle):
  def __init__(self, sprite: list[str], pos: tuple[int, int], scoreboard: Scoreboard):
    super().__init__()
    self.sprites = sprite
    self.curSprite = 0
    self.shape(self.sprites[0])
    self.penup()
    self.color("green")
    self.speed("fastest")
    self.alive = True
    self.goto(pos)
    self.scoreboard = scoreboard
  
  def move(self, dir):
    self.changeSprite()
    self.goto(self.pos()[0] + (MOVE_X * dir), self.pos()[1])
  
  def moveDown(self):
    self.changeSprite()
    self.goto(self.pos()[0], self.pos()[1] - MOVE_Y)
  
  def blowUp(self):
    if(self.alive):
      self.scoreboard.addScore(100)
      self.alive = False
      self.shape(EXPLODE_SPRITE)
  
  def changeSprite(self):
    self.curSprite += 1
    self.curSprite = self.curSprite % len(self.sprites)
    self.shape(self.sprites[self.curSprite])