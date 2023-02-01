from turtle import Turtle
from time import sleep

POSITION = (0,-395)
FONT = "Courier"

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("green")
    self.shape("blank")
    self.penup()
    self.goto(POSITION)
    self.speed("fastest")
    self.score = 0
    self.lives = 3
    self.addScore(0)

  def addScore(self, increaseAmount):
    self.clear()
    self.score += increaseAmount
    self.write(f"Lives: {self.lives} | Score: {self.score}", align="center", font=(FONT, 24, "normal"))

  def gameOver(self):
    self.clear()
    self.write(f"Game Over.  Final Score - {self.score}", align="center", font=(FONT, 18, "normal"))
    
  def message(self, text):
    self.clear()
    self.write(text, align="center", font=(FONT, 24, "normal"))
  
  def countdown(self, startNum: int):
    for i in range(startNum, 1, -1):
      self.message(f"{i}")
      sleep(1)
    self.addScore(0)