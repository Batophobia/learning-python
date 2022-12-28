import random
from tools import cls, getOneOfThese

class Card:
  def __init__(self, name, values: list, suit):
    self.name = name
    self.values = values
    self.suit = suit
  def borderString(self):
    return f"+----+"
  def topString(self):
    return f"|   {self.suit}|"
  def toString(self):
    return f"| {self.name if len(self.name) == 2 else (' ' + self.name) } |"
  def bottomString(self):
    return f"|{self.suit}   |"
  def backString(self):
    return f"|####|"


# clubs (♣), diamonds (♦), hearts (♥), spades (♠)
deck: list[Card] = [
  Card("A", [1,11], "♣"),
  Card("2", [2], "♣"),
  Card("3", [3], "♣"),
  Card("4", [4], "♣"),
  Card("5", [5], "♣"),
  Card("6", [6], "♣"),
  Card("7", [7], "♣"),
  Card("8", [8], "♣"),
  Card("9", [9], "♣"),
  Card("10", [10], "♣"),
  Card("J", [10], "♣"),
  Card("Q", [10], "♣"),
  Card("K", [10], "♣"),
  Card("A", [1,11], "♦"),
  Card("2", [2], "♦"),
  Card("3", [3], "♦"),
  Card("4", [4], "♦"),
  Card("5", [5], "♦"),
  Card("6", [6], "♦"),
  Card("7", [7], "♦"),
  Card("8", [8], "♦"),
  Card("9", [9], "♦"),
  Card("10", [10], "♦"),
  Card("J", [10], "♦"),
  Card("Q", [10], "♦"),
  Card("K", [10], "♦"),
  Card("A", [1,11], "♥"),
  Card("2", [2], "♥"),
  Card("3", [3], "♥"),
  Card("4", [4], "♥"),
  Card("5", [5], "♥"),
  Card("6", [6], "♥"),
  Card("7", [7], "♥"),
  Card("8", [8], "♥"),
  Card("9", [9], "♥"),
  Card("10", [10], "♥"),
  Card("J", [10], "♥"),
  Card("Q", [10], "♥"),
  Card("K", [10], "♥"),
  Card("A", [1,11], "♠"),
  Card("2", [2], "♠"),
  Card("3", [3], "♠"),
  Card("4", [4], "♠"),
  Card("5", [5], "♠"),
  Card("6", [6], "♠"),
  Card("7", [7], "♠"),
  Card("8", [8], "♠"),
  Card("9", [9], "♠"),
  Card("10", [10], "♠"),
  Card("J", [10], "♠"),
  Card("Q", [10], "♠"),
  Card("K", [10], "♠"),
]

player = []
playerTotals: list[int] = []
dealer = []
dealerTotals: list[int] = []

def totalCards(cards: list[Card]):
  totals = [0]
  for card in cards:
    if len(card.values) > 1:
      for i in range(len(totals)):
        totals.append(totals[i] + card.values[1])
        totals[i] += card.values[0]
    else:
      for i in range(len(totals)):
        totals[i] += card.values[0]
  return totals

def displayCards(cards: list[Card], hideFirst = True):
  if len(cards) < 1: return

  display = ""
  for card in cards:
    display += card.borderString()
  display += "\n"
  for card in cards:
    if hideFirst and cards.index(card) == 0:
      display += card.backString()
    else:
      display += card.topString()
  display += "\n"
  for card in cards:
    if hideFirst and cards.index(card) == 0:
      display += card.backString()
    else:
      display += card.toString()
  display += "\n"
  for card in cards:
    if hideFirst and cards.index(card) == 0:
      display += card.backString()
    else:
      display += card.bottomString()
  display += "\n"
  for card in cards:
    display += card.borderString()
  print(display)

runAgain = True
keepGoing = False
lostGame = False
while runAgain:
  cls()
  
  if not keepGoing:
    random.shuffle(deck)
    lostGame = False
    player = []
    dealer = []
    player.append(deck.pop())
    dealer.append(deck.pop())
    dealer.append(deck.pop())
  
  player.append(deck.pop())
  
  dealerTotals = totalCards(dealer)
  playerTotals = totalCards(player)
  playerTotals = list(filter(lambda t: t < 22, playerTotals))
  
  print("-- Dealer --")
  displayCards(dealer, len(playerTotals) > 0)
  print("-- You --")
  displayCards(player, False)

  if len(playerTotals) < 1:
    lostGame = True
    print("Bust.")
  else:
    print(playerTotals)

  if len(playerTotals) > 0 and input(f"Would you like to hit (Y/n)? ").lower() == "y":
    keepGoing = True
  else:
    keepGoing = False
    if not lostGame:
      cls()  

      while len(list(filter(lambda t: t > 15, totalCards(dealer)))) < 1:
        dealer.append(deck.pop())
      
      print("-- Dealer --")
      displayCards(dealer, False)
      print("-- You --")
      displayCards(player, False)

      dealerTotals = list(filter(lambda t: t < 22, totalCards(dealer)))
      if len(dealerTotals) < 1:
        print("Dealer busts.  You win.")
      elif max(dealerTotals) < max(playerTotals):
        print(f"You win {max(playerTotals)} to {max(dealerTotals)}.")
      else:
        print(f"Dealer wins {max(dealerTotals)} to {max(playerTotals)}.")
    for card in player:
      deck.append(card)
    for card in dealer:
      deck.append(card)
    if input("Would you like to play again (Y/n)? ").lower() != "y":
      runAgain = False