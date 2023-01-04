import time
from turtle import Screen
from Frogger.player import Player
from Frogger.car_manager import CarManager
from Frogger.car import Car
from Frogger.scoreboard import Scoreboard

SCREEN_SIZE = 600
GRID_SIZE = 30
FINISH_LINE_Y = 270

screen = Screen()
screen.setup(width = SCREEN_SIZE, height = SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Frogger")
screen.tracer(0)

player = Player(GRID_SIZE, FINISH_LINE_Y)
score = Scoreboard()
cars = CarManager(GRID_SIZE, FINISH_LINE_Y - GRID_SIZE, SCREEN_SIZE/2)

screen.onkey(player.moveUp, "Up")
screen.onkey(player.moveLeft, "Left")
screen.onkey(player.moveRight, "Right")
screen.onkey(player.moveDown, "Down")
screen.listen()

game_is_on = True
while game_is_on:
  cars.update()
  time.sleep(0.02)
  screen.update()
  if(cars.checkSquish(player.pos())):
    score.gameOver()
    game_is_on = False
  if player.finished():
    player.reset()
    cars.reset()
    score.addLevel()

screen.exitonclick()