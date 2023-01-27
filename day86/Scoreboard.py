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
    self.level = 1
    self.updateUI()

  def updateUI(self):
    self.clear()
    self.write(f"{self.level}", align="center", font=(FONT, 24, "normal"))

  def addLevel(self):
    self.level += 1
    self.updateUI()
  
  def gameOver(self):
    self.clear()
    self.write(f"Game Over.  Final Level - {self.level}", align="center", font=(FONT, 18, "normal"))
    
  def message(self, text):
    self.clear()
    self.write(text, align="center", font=(FONT, 24, "normal"))
