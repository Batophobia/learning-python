from turtle import Screen, Shape
from tkinter import PhotoImage

ENEMY_SPRITES = [
    [r".\Invaders\Enemy0-0.gif", r".\Invaders\Enemy0-1.gif"],
    [r".\Invaders\Enemy1-0.gif", r".\Invaders\Enemy1-1.gif"],
    [r".\Invaders\Enemy2-0.gif", r".\Invaders\Enemy2-1.gif"],
    [r".\Invaders\Enemy3.gif"],
  ]
EXPLODE_SPRITE = r".\Invaders\Explode.gif"

ZOOM = 3

class GameAssets():
  def __init__(self, window: Screen):
    for style in ENEMY_SPRITES:
      for sprite in style:
        self.addShape(window, sprite)
    window.addshape(EXPLODE_SPRITE)
  
  def addShape(self, window: Screen, sprite: str):
    larger = PhotoImage(file=sprite).zoom(ZOOM, ZOOM)
    window.addshape(sprite, Shape("image", larger))