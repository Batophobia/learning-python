import turtle
import time
from Invaders.GameAssets import GameAssets
from Invaders.Player import Player
from Invaders.EnemyManager import EnemyManager
from Invaders.BulletManager import BulletManager
from Invaders.Scoreboard import Scoreboard

INITIAL_LENGTH = 3
COLLECTION_RANGE = 15
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
GAME_WIDTH = 350
GAME_HEIGHT = 350

def main():
  window = turtle.Screen()
  window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
  window.screensize(GAME_WIDTH, GAME_HEIGHT)
  window.bgcolor("black")
  window.title("Invaders")
  window.colormode(255)
  window.tracer(0)

  # Load sprites
  GameAssets(window)

  bullets = BulletManager(window.screensize())
  score = Scoreboard()
  player = Player(window, bullets, score)
  enemies = EnemyManager(window.screensize(), bullets, score)
  
  window.update()
  isAlive = True
  score.countdown(5)
  while isAlive:
    onBottom = enemies.move()
    if(onBottom):
      isAlive = False
    
    bullets.move()
    bullets.check(player)
    for enemy in enemies.enemies:
      bullets.check(enemy)
    
    player.tick()
    if(player.lives < 1):
      isAlive = False

    window.update()
    time.sleep(.01)
    
    if(len(enemies.enemies) < 1):
      isAlive = False
  
  score.gameOver()
  window.exitonclick()

if __name__ == "__main__":
  main()