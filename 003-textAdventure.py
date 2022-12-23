rooms = [
  ["You awake in a dungeon cell.  The door to the cell is open.  Options:\n 1) Leave cell\n 2) Examine surroundings\n", 1, 2]
  , ["You exit your cell to find a long hallway.  Options:\n 1) Return to cell\n 2) Head North\n 3) Head South\n", 0, 3, 4]
  , ["You examine your cell.  There's nothing here.  Not even a bed.  Options:\n 1) Leave cell\n", 1]
  , ["Traveling North, you stumble upon the guard.  He's quite angry at your escape attempt.  He raises his mideval mace and strikes you down.  You have died.", -1]
  , ["Traveling South, you head up a stairway, emerging in a well lit tavern.  The barkeeper invites you over for a drink.  Success! You've escaped the dungeon.", -2]
]

curRoom = 0
isAlive = True
isPlaying = True
while(isAlive & isPlaying):
  if(rooms[curRoom][1] == -1):
    isAlive = False
    print(str(rooms[curRoom][0]))
  elif(rooms[curRoom][1] == -2):
    isPlaying = False
    print(str(rooms[curRoom][0]))
  else:
    inpt = int(input(rooms[curRoom][0]))
    if(inpt < len(rooms[curRoom])):
      curRoom = rooms[curRoom][inpt]
  