import turtle

INITIAL_LENGTH = 3
MOVE_AMOUNT = 20

class Snake:
  def __init__(self, startLength = INITIAL_LENGTH):
    self.snake = []
    for i in range(startLength):
      temp = turtle.Turtle("square")
      temp.color("white")
      temp.penup()
      temp.goto(20 * -i, 0)
      self.snake.append(temp)
    
    self.head = self.snake[0]
  
  def move(self):
    for i in range(len(self.snake) - 1, 0, -1):
      self.snake[i].goto(self.snake[i-1].pos())
    self.head.forward(MOVE_AMOUNT)
  
  def turnUp(self):
    if(self.head.heading() != 270):
      self.head.setheading(90)
  def turnLeft(self):
    if(self.head.heading() != 0):
      self.head.setheading(180)
  def turnRight(self):
    if(self.head.heading() != 180):
      self.head.setheading(0)
  def turnDown(self):
    if(self.head.heading() != 90):
      self.head.setheading(270)
