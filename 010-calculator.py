def add(x, y):
  return x + y
def subtract(x, y):
  return add(x, -y)
def multiply(x, y):
  return x * y
def divide(x, y):
  return x / y

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

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

def getOp(message):
  userInput = ""
  while not checkKey(operations, userInput):
    userInput = input(message)
  return userInput

runAgain = True
keepGoing = False
while runAgain:
  if not keepGoing:
    num1 = getNum("What is the first number? ")
  for op in operations:
    print(op)
  user = getOp("Pick an operation: ")
  num2 = getNum("What is the next number? ")
  
  result = operations[user](num1, num2)
  print(f"{num1} {user} {num2} = {result}")
  
  if input(f"Would you like to continue using {result} (Y/n)? ").lower() == "y":
    num1 = result
    keepGoing = True
  elif input("Would you like to run again (Y/n)? ").lower() == "y":
    keepGoing = False
  else:
    runAgain = False