from tools import cls, getOneOfThese, getNum
import time

FLAVORS = [
  { "name": "Espresso", "water": 50, "coffee": 18, "milk": 0, "price": 1.5 },
  { "name": "Latte", "water": 200, "coffee": 24, "milk": 150, "price": 2.5 },
  { "name": "Cappuccino", "water": 250, "coffee": 24, "milk": 100, "price": 3.0 },
]

COINS = [
  { "name": "penny", "val": .01 },
  { "name": "nickel", "val": .05 },
  { "name": "dime", "val": .1 },
  { "name": "quarter", "val": .25 },
]

waterLevel = 300
milkLevel = 200
coffeeLevel = 100
money = 0.0

def addResource(resource, amount):  
  global waterLevel
  global coffeeLevel
  global milkLevel
  global money

  if resource == "water":
    waterLevel += amount
  elif resource == "milk":
    coffeeLevel += amount
  elif resource == "coffee":
    milkLevel += amount
  elif resource == "money":
    money += amount


def getFlavor(name):
  for flavor in FLAVORS:
    if flavor["name"].lower() == name.lower():
      return flavor

def printFlavors():
  for flavor in FLAVORS:
    print(f'{flavor["name"]}: ${flavor["price"]}0')

def printCoins():
  idx = 0
  for coin in COINS:
    idx += 1
    print(f'{idx}) Insert {coin["name"]}')

def flavorNames():
  retVal = []
  for flavor in FLAVORS:
    retVal.append(flavor["name"])
  return retVal

def printLevels():
  print(f'Water remaining: {waterLevel} ml')
  print(f'Milk remaining: {milkLevel} ml')
  print(f'Coffee remaining: {coffeeLevel} g')
  print('Money: ${:0.2f}'.format(money))

def checkLevels(flavor):
  isGood = True
  if waterLevel < flavor["water"]:
    print(f'Water level too low')
    isGood = False
  if coffeeLevel < flavor["coffee"]:
    print(f'Coffee level too low')
    isGood = False
  if milkLevel < flavor["milk"]:
    print(f'Milk level too low')
    isGood = False
  return isGood

def makeDrink(flavor):
  addResource("water", -flavor["water"])
  addResource("coffee", -flavor["coffee"])
  addResource("milk", -flavor["milk"])
  addResource("money", flavor["price"])
  print(f"Enjoy your {flavor['name']}")

runAgain = True
while runAgain:
  cls()
  printFlavors()
  user = getOneOfThese("What kind of coffee do you want?\n", [*flavorNames(), "report", "fill", "exit"])
  if user == "report":
    printLevels()
    input("Press any key to continue.")
  elif user == "exit":
    runAgain = False
  elif user == "fill":
    user = getOneOfThese("Did you add [water], [milk], or [coffee]? ", ["water","milk","coffee"])
    amount = getNum(f"How much {user} was added? ")
    addResource(user.lower(), amount)
  else:
    choice = getFlavor(user)
    if(checkLevels(choice)):
      total = 0.0
      while total < choice["price"]:
        cls()
        print('Please insert ${:0.2f}.'.format(choice["price"] - total))
        printCoins()
        coin = int(getOneOfThese("", [str(i) for i in range(1, len(COINS) + 1)]))
        total += COINS[coin - 1]["val"]
      if total - choice["price"] > 0:
        print("Your change is ${:0.2f}".format(total - choice["price"]))
      makeDrink(choice)
    time.sleep(5)