from turtle import Turtle

POSITION = (-290,260)
FONT = "Courier"

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("yellow")
    self.shape("blank")
    self.penup()
    self.goto(POSITION)
    self.speed("fastest")
    self.level = 1
    self.updateUI()

  def updateUI(self):
    self.clear()
    self.write(f"Level {self.level}", align="left", font=(FONT, 24, "normal"))

  def addLevel(self):
    self.level += 1
    self.updateUI()
  
  def gameOver(self):
    self.clear()
    self.write(f"Game Over.  Level {self.level}", align="left", font=(FONT, 18, "normal"))
    
  def message(self, text):
    self.clear()
    self.write(text, align="left", font=(FONT, 24, "normal"))
