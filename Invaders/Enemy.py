from turtle import Turtle
from random import randint

MOVE_X = 10
MOVE_Y = 20

class Enemy(Turtle):
  def __init__(self, sprite: list[str], pos: tuple[int, int]):
    super().__init__()
    self.sprites = sprite
    self.curSprite = 0
    self.shape(self.sprites[0])
    self.penup()
    self.color("green")
    self.speed("fastest")
    self.pos = pos
    self.goto(pos)
  
  def move(self, dir):
    self.changeSprite()
    self.pos = (self.pos[0] + (MOVE_X * dir), self.pos[1])
    self.goto(self.pos)
  
  def moveDown(self):
    self.changeSprite()
    self.pos = (self.pos[0], self.pos[1] - MOVE_Y)
    self.goto(self.pos)
  
  def changeSprite(self):
    self.curSprite += 1
    self.curSprite = self.curSprite % len(self.sprites)
    self.shape(self.sprites[self.curSprite])
