import os

bids = {}

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

runAgain = True
while runAgain:
  clear()
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  
  bids[name] = bid

  user = input("Is there another bidder (Y/n)? ").lower()
  if user != "y":
    runAgain = False

winner = ""
for bid in bids:
  if winner =="":
    winner = bid
  elif bids[bid] > bids[winner]:
    winner = bid

print(f"The winner is {winner} for ${bids[winner]}")