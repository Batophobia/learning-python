import random
from tools import getNum, getOneOfThese

MIN_NUM = 1
MAX_NUM = 100

runAgain = True
keepGoing = True
while runAgain:
  diff = getOneOfThese(f"I'll think of a number between {MIN_NUM} and {MAX_NUM}.  Your goal is to guess it.\nWould you like to play on [easy] or [hard]?\n", ["easy", "e", "hard", "h"])
  if diff == "hard" or diff == "h":
    guesses = 6
  else:
    guesses = 12
  
  num = random.randint(MIN_NUM, MAX_NUM)
  while keepGoing:
    user = getNum(f"You have {guesses} guesses left.  What number am I thinking of? ")
    if user > num:
      print("That number is too high.")
      guesses -= 1
    elif user < num:
      print("That number is too low.")
      guesses -= 1
    else:
      print("That's the number!")
      keepGoing = False
    if guesses < 1:
      print(f"That's all your guesses.  My number was {num}.")
      keepGoing = False
    
  if input("Would you like to run again (Y/n)? ").lower() == "y":
    keepGoing = True
  else:
    runAgain = False