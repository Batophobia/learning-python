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
    self.left = 0
    self.right = 0
    self.updateUI()

  def updateUI(self):
    self.clear()
    self.write(f"{self.left}  |  {self.right}", align="center", font=(FONT, 24, "normal"))

  def addLeft(self):
    self.left += 1
    self.updateUI()
  def addRight(self):
    self.right += 1
    self.updateUI()

  def gameOver(self):
    self.clear()
    self.write(f"Game Over.  Final Score - {self.score}", align="center", font=(FONT, 18, "normal"))
    
  def message(self, text):
    self.clear()
    self.write(text, align="center", font=(FONT, 24, "normal"))
