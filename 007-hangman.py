import random
from hangman_words import word_list as wordList
from hangman_art import stages

selected = ""
display = ""
playing = True
wrongs = 0


def userGuess():
  guess = input("Guess a letter: ").lower()
  while len(guess) != 1:
    guess = input("Guess a single letter: ").lower()
  
  global selected
  indexes = [pos for pos, char in enumerate(selected) if char == guess]
  
  global playing
  if len(indexes) > 0:
    global display
    for idx in indexes:
      display = display[:idx] + selected[idx] + display[idx + 1:]
    if display == selected:
      print(f"You Win!  The word was {selected}.")
      playing = False
  else:
    global wrongs
    wrongs += 1
    if wrongs >= len(stages) - 1:
      playing = False
      ui()
      print(f"You Lose.  The word was {selected}.")
    else:
      print("Wrong")

def ui():
  print(stages[wrongs])
  print(display)

def initGame():
  global display
  display = ""
  global selected
  selected = wordList[random.randint(0, len(wordList) - 1)]
  for letter in selected:
    display += "_"
  global wrongs
  wrongs = 0

def playAgain():
  user = input("Play again (Y/n)?  ").lower()
  return user == "y"


while playing or playAgain():
  playing = True
  initGame()
  while(playing):
    ui()
    userGuess()