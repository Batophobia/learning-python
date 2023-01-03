from turtle import Turtle

POSITION = (0,250)
FONT = "Courier"

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("yellow")
    self.shape("blank")
    self.penup()
    self.goto(POSITION)
    self.speed("fastest")
    self.score = 0
    self.addScore(0)

  def addScore(self, increaseAmount):
    self.clear()
    self.score += increaseAmount
    self.write(f"Score: {self.score}", align="center", font=(FONT, 24, "normal"))

  def gameOver(self):
    self.clear()
    self.write(f"Game Over.  Final Score - {self.score}", align="center", font=(FONT, 18, "normal"))
    
  def message(self, text):
    self.clear()
    self.write(text, align="center", font=(FONT, 24, "normal"))
