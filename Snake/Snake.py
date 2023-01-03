import turtle

INITIAL_LENGTH = 3
MOVE_AMOUNT = 20
COLLISION_DISTANCE = 5

class Snake:
  def __init__(self, startLength = INITIAL_LENGTH):
    self.snake = []
    for i in range(startLength):
      self.grow()
    
    self.head = self.snake[0]
  
  def move(self):
    for i in range(len(self.snake) - 1, 0, -1):
      self.snake[i].goto(self.snake[i-1].pos())
    self.head.forward(MOVE_AMOUNT)
  
  def grow(self):
    temp = turtle.Turtle("square")
    temp.color("white")
    temp.penup()
    if(len(self.snake)):
      temp.goto(self.snake[len(self.snake)-1].pos())
    else:
      temp.goto(0,0)
    self.snake.append(temp)

  def detectCollision(self):
    for body in self.snake[1:]:
      if self.head.distance(body) < COLLISION_DISTANCE:
        return True
    return False

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
