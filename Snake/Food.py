from turtle import Turtle
from random import randint

POINTS = 1
SCREEN_SIZE = 300
FOOD_SIZE = 10

class Food(Turtle):
  def __init__(self, points = POINTS):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(FOOD_SIZE/20, FOOD_SIZE/20)
    self.color("red")
    self.speed("fastest")
    self.points = points
    self.move()

  def move(self):
    self.goto(randint(-SCREEN_SIZE + FOOD_SIZE, SCREEN_SIZE - FOOD_SIZE), randint(-SCREEN_SIZE + FOOD_SIZE, SCREEN_SIZE - FOOD_SIZE))
  
  def pickup(self):
    self.move()
    return self.points
