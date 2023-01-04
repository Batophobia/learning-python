from random import randint
from Frogger.car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_CARS = 10
CAR_TICK = 10

class CarManager:    
  def __init__(self, gridSize, yMax, xMax):
    self.spacing = gridSize
    self.xMax = xMax
    self.yMax = yMax
    self.yMin = -yMax
    self.cars = []
    self.maxCars = START_CARS
    self.reset()

  def reset(self):
    for car in self.cars:
      car.delete()
    self.cars = []
    self.carTick = CAR_TICK
    self.maxCars += 2
    self.spawnCar()
  
  def spawnCar(self):
    if len(self.cars) >= self.maxCars:
      self.cars[0].markForPop()
    
    ypos = randint(self.yMin / self.spacing, self.yMax / self.spacing)
    clr = COLORS[randint(0,len(COLORS)-1)]
    goinLeft = ypos % 2 == 0
    if goinLeft:
      startPos = (self.xMax + self.spacing, ypos * self.spacing)
    else:
      startPos = (-self.xMax - self.spacing, ypos * self.spacing)
    car = Car(startPos, clr, goinLeft)
    self.cars.append(car)

  def update(self):
    self.carTick -= 1
    if self.carTick <= 0:
      self.carTick = CAR_TICK
      self.spawnCar()
    for car in self.cars:
      if car.move(self.xMax):
        self.cars.pop(0)

  def checkSquish(self, pos):
    for car in self.cars:
      if car.checkSquish(pos, self.spacing):
        return True
    return False