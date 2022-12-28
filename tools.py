import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def checkKey(dic, key):
  return key in dic.keys()

def isNumber(val):
  try:
    float(val)
    return True
  except ValueError:
    return False

def getNum(message):
  userInput = ""
  while not isNumber(userInput):
    userInput = input(message)
  return float(userInput)

def getOneOfThese(message, options):
  userInput = "ݧܔthis is ㍌definitely not an ⣯option in the list of options♥ꔰ"
  while userInput not in options:
    userInput = input(message)
  return userInput