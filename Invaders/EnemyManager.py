from Invaders.Enemy import Enemy
from Invaders.GameAssets import ENEMY_SPRITES
from Invaders.BulletManager import BulletManager
from Invaders.Scoreboard import Scoreboard
from random import randint

X_BUFFER = 50
Y_BUFFER = 35
MAX_DELAY = 10
SPRITE_PADDING = 40
NUM_ROW = 5
NUM_COL = 11
SHOOT_TIMER = 20

class EnemyManager():
  def __init__(self, gameSize: tuple[int,int], bullets: BulletManager, score: Scoreboard):
    self.dir = 1
    self.gameSize = gameSize
    self.moveDelay = MAX_DELAY
    self.moveTimer = self.moveDelay
    self.shootDelay = SHOOT_TIMER
    self.shootTimer = self.shootDelay
    self.reverse = False
    self.score = score
    self.bullets = bullets
    self.resetEnemies()
    
  def resetEnemies(self):
    self.enemies = []
    xMax = self.gameSize[0] # - X_BUFFER
    yMax = self.gameSize[1] # - Y_BUFFER
    for y in range(1, NUM_ROW+1, 1):
      for x in range(1, NUM_COL+1, 1):
        self.spawn(x * X_BUFFER - xMax, y * Y_BUFFER + yMax / 2, int((y-1)/2))
  
  def spawn(self, x: int, y: int, style: int):
    enemy = Enemy(ENEMY_SPRITES[style], (x, y), self.score)
    self.enemies.append(enemy)

  def shoot(self):
    self.shootTimer = self.shootDelay
    self.bullets.spawn(self.enemies[randint(0, len(self.enemies) - 1)].pos(), False)

  def move(self):
    self.moveDelay = len(self.enemies) / (NUM_ROW * NUM_COL) * MAX_DELAY
    self.moveTimer -= 1

    self.shootDelay = len(self.enemies) / (NUM_ROW * NUM_COL) * SHOOT_TIMER
    self.shootTimer -= 1
    if self.shootTimer < 1: self.shoot()

    if self.moveTimer > 0: return

    self.moveTimer = self.moveDelay
    if self.reverse:
      self.reverse = False
      self.dir *= -1
      for enemy in self.enemies:
        enemy.moveDown()
        if(enemy.pos()[1] <= -self.gameSize[1]):
          return True
    else:
      toRemove = []
      for enemy in self.enemies:
        if(enemy.alive):
          enemy.move(self.dir)
          if(abs(enemy.pos()[0]) + SPRITE_PADDING >= self.gameSize[0]):
            self.reverse = True
        else:
          enemy.hideturtle()
          toRemove.append(enemy)
          
      for e in toRemove:
        self.enemies.remove(e)
