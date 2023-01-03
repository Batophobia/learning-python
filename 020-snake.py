import turtle
import time
from Snake.Snake import Snake
from Snake.Food import Food
from Snake.Scoreboard import Scoreboard

INITIAL_LENGTH = 3
COLLECTION_RANGE = 15
GAME_SIZE = 300

window = turtle.Screen()
window.setup(width=GAME_SIZE*2,height=GAME_SIZE*2)
window.bgcolor("black")
window.title("Snake")
window.colormode(255)
window.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

window.onkey(snake.turnUp, "Up")
window.onkey(snake.turnLeft, "Left")
window.onkey(snake.turnRight, "Right")
window.onkey(snake.turnDown, "Down")
window.listen()

def main():
  window.update()
  isAlive = True

  for i in range(5,1,-1):
    score.message(f"{i}")
    time.sleep(1)
  score.addScore(0)

  while isAlive:
    snake.move()
    window.update()
    time.sleep(.05)
    if snake.head.distance(food) < COLLECTION_RANGE:
      score.addScore(food.pickup())
      snake.grow()
    
    if snake.head.xcor() >= GAME_SIZE or snake.head.xcor() <= -GAME_SIZE or snake.head.ycor() >= GAME_SIZE or snake.head.ycor() <= -GAME_SIZE:
      isAlive = False
    if snake.detectCollision():
      isAlive = False

  score.gameOver()
  window.exitonclick()

if __name__ == "__main__":
  main()