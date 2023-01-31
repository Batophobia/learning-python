import turtle
import time
from Invaders.GameAssets import GameAssets
from Invaders.Player import Player
from Invaders.EnemyManager import EnemyManager
from Invaders.Scoreboard import Scoreboard

INITIAL_LENGTH = 3
COLLECTION_RANGE = 15
GAME_WIDTH = 700
GAME_HEIGHT = 800

def main():
  window = turtle.Screen()
  window.setup(width=GAME_WIDTH,height=GAME_HEIGHT)
  window.bgcolor("black")
  window.title("Invaders")
  window.colormode(255)
  window.tracer(0)

  # Load sprites
  GameAssets(window)

  player = Player(window)
  score = Scoreboard()
  enemies = EnemyManager((GAME_WIDTH,GAME_HEIGHT))

  window.update()
  isAlive = True
  timer=0
  while isAlive:
    enemies.move()
    window.update()
    time.sleep(.1)
    timer += 1

    if(timer > 9999):
      isAlive = False
    

  score.gameOver()
  window.exitonclick()

if __name__ == "__main__":
  main()