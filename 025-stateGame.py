from random import randint
import pandas
import turtle

def main():
  bgImage = "States/blank_states_img.gif"
  window = turtle.Screen()
  window.addshape(bgImage)
  turtle.shape(bgImage)
  window.title("State Quiz")
  ui = turtle.Turtle()
  ui.shape("blank")
  ui.penup()
  states = pandas.read_csv("States/50_states.csv")
  correct = []

  while len(correct) < 50:
    answer = window.textinput(title=f"{len(correct)}/50 States", prompt="Name any state")
    answer = answer.title()
    if answer not in correct and answer in states["state"].tolist():
      correct.append(answer)
      stateInfo = states[states.state == answer]
      ui.setpos(int(stateInfo.x), int(stateInfo.y))
      ui.write(answer, align="center", font=("Arial", 10, "normal"))


if __name__ == "__main__":
  main()