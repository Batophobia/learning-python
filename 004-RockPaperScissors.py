import random

options = [
  "Rock"
  , "Paper"
  , "Scissors"
]

opp = random.randint(0,2)
result = 0
inpt = 0

while(inpt < 1 or inpt > 3):
  inpt = int(input("1) ROCK\n2) PAPER\n3) SCISSORS\n"))

output = "Opponent selected "
if(opp == 0):
  output += "ROCK."
  if(inpt == 2):
    result = 1
  elif(inpt == 3):
    result = -1
elif(opp == 1):
  output += "PAPER."
  if(inpt == 1):
    result = -1
  elif(inpt == 3):
    result = 1
else:
  output += "SCISSORS."
  if(inpt == 1):
    result = 1
  elif(inpt == 2):
    result = -1

if(result == -1):
  print(output + " You lose.")
elif(result == 1):
  print(output + " You win!")
else:
  print(output + " It's a tie.")