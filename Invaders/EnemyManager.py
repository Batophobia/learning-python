from Invaders.Enemy import Enemy
import Invaders.GameAssets as GameAssets

X_BUFFER = 100
Y_BUFFER = 100
MAX_DELAY = 10
SPRITE_PADDING = 40

class EnemyManager():
  def __init__(self, gameSize: tuple[int,int]):
    self.dir = 1
    self.gameSize = gameSize
    self.moveDelay = MAX_DELAY
    self.moveTimer = self.moveDelay
    self.reverse = False
    self.resetEnemies()
    
  def resetEnemies(self):
    self.enemies = []
    style = 2
    xMax = int(self.gameSize[0] / 2) - X_BUFFER
    yMax = int(self.gameSize[1] / 2) - Y_BUFFER
    for y in range(yMax, 0, -int(yMax / (len(GameAssets.ENEMY_SPRITES) + 1))):
      for x in range(xMax, -xMax, -int(xMax * 2 / 11)):
        self.spawn(x, y, round(y/100) - 1)
  
  def spawn(self, x: int, y: int, style: int):
    enemy = Enemy(GameAssets.ENEMY_SPRITES[style], (x, y))
    self.enemies.append(enemy)

  def move(self):
    self.moveTimer -= 1
    if self.moveTimer > 0: return

    self.moveTimer = self.moveDelay
    if self.reverse:
      self.reverse = False
      self.dir *= -1
      for enemy in self.enemies:
        enemy.moveDown()
    else:
      for enemy in self.enemies:
        enemy.move(self.dir)
        if(abs(enemy.pos[0]) + SPRITE_PADDING >= self.gameSize[0] / 2):
          self.reverse = True
  
  def pickup(self):
    self.move()
    return self.points
