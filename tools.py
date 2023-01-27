import os

def cls():
  """Clear the console"""
  os.system('cls' if os.name == 'nt' else 'clear')

def checkKey(dic, key):
  """Check if a given dictionary contains a specific key"""
  return key in dic.keys()

def isNumber(val):
  """Check if a given value is a number"""
  try:
    float(val)
    return True
  except ValueError:
    return False

def getNum(message):
  """Repeat input until given a valid number"""
  userInput = ""
  while not isNumber(userInput):
    userInput = input(message)
  return float(userInput)

def getOneOfThese(message, options, ignoreCase = True):
  """Repeat input until given one of a list of options"""
  userInput = "ݧܔthis is ㍌definitely not an ⣯option in the list of options♥ꔰ"
  if ignoreCase:
    while userInput not in [option.lower() for option in options]:
      userInput = input(message).lower()
    return userInput
  else:
    while userInput not in options:
      userInput = input(message)
    return userInput

def getFullPath():
  return os.path.abspath(os.path.dirname(__file__))