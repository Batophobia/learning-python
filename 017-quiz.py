import random
from quiz_questions import questions
from tools import getOneOfThese

class Question:
  def __init__(self, questionText, isTrue: bool):
    self.text = questionText
    self.answer = isTrue
  
  def display(self):
    print(self.text)

NUM_QUESTIONS = 5
def getQuiz(questionList):
  random.shuffle(questionList)
  quiz = questionList[0:NUM_QUESTIONS]
  return quiz

def main():
  runAgain = True
  while runAgain:
    quiz = getQuiz(questions)
    numRight = 0
    for q in quiz:
      question = Question(q["text"], q["isTrue"])
      print("[True] or [False]")
      question.display()
      user = getOneOfThese("",["true", "t", "false", "f", "yes", "no", "y", "n", "1", "0"])
      user = (user == "true" or user == "t" or user == "yes" or user == "y" or user == "1")
      if user == question.answer:
        numRight += 1
    if input(f"You got {numRight} of {NUM_QUESTIONS} correct ({(numRight / NUM_QUESTIONS * 100):0.0f}%).  Play again (Y/n)? ").lower() != "y":
      runAgain = False

if __name__ == "__main__":
  main()