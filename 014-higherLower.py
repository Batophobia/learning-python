import random
import requests
from tools import cls, getOneOfThese

def pullList():
  url = 'https://api.stackexchange.com/2.3/questions?pagesize=100&order=desc&sort=votes&site=stackoverflow'
  headers = {'user-agent': 'my-app/0.0.1'}
  response = requests.get(url, headers=headers)
  #print(response.json())
  return list(map(
    reduceResponse
    , response.json()["items"]
  ))

def reduceResponse(resp):
  return { "title": resp["title"], "view_count": resp["view_count"], "score": resp["score"] }

diffList = pullList()

runAgain = True
keepGoing = True
while runAgain:
  score = 0
  
  while keepGoing:
    side1 = random.randint(0, len(diffList) - 1)
    side2 = random.randint(0, len(diffList) - 1)
    while diffList[side1]["score"] == diffList[side2]["score"]:
      side2 = (side2 + 1) % len(diffList)
    
    print(f"1) {diffList[side1]['title']}")
    print(f"2) {diffList[side2]['title']}")
    user = getOneOfThese("Which of these Stack Overflow questions has a higher score? ", ["1", "2"])
    cls()
    if user == "1" and diffList[side1]["score"] > diffList[side2]["score"]:
      score += 1
      print(f'Correct.  The first one has a score of {diffList[side1]["score"]}')
    elif user == "2" and diffList[side1]["score"] < diffList[side2]["score"]:
      score += 1
      print(f'Correct.  The second one has a score of {diffList[side2]["score"]}')
    else:
      print(f'Incorrect.  The first one has a score of {diffList[side1]["score"]} and the second one has a score of {diffList[side2]["score"]}.  You correctly chose {score} times')
      keepGoing = False
    
  if input("Would you like to run again (Y/n)? ").lower() == "y":
    keepGoing = True
  else:
    runAgain = False