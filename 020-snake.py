import turtle
import random
import time
from Snake.Snake import Snake

window = turtle.Screen()
window.setup(width=600,height=600)
window.bgcolor("black")
window.title("Snake")
window.colormode(255)
window.tracer(0)

FORWARD_AMOUNT = 10
def moveForward():
  leo.forward(FORWARD_AMOUNT)

INITIAL_LENGTH = 3

snake = Snake()

window.onkey(snake.turnUp, "Up")
window.onkey(snake.turnLeft, "Left")
window.onkey(snake.turnRight, "Right")
window.onkey(snake.turnDown, "Down")
window.listen()


def main():
  window.update()
  isAlive = True

  while isAlive:
    snake.move()
    window.update()
    time.sleep(.02)

  window.exitonclick()

if __name__ == "__main__":
  main()