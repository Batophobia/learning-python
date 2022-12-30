import turtle

def changeColor(turt, color):
  turt.color(color)

def moveTurtle(turt, distance: int):
  turt.forward(distance)

def main():
  donny = turtle.Turtle()
  donny.shape("turtle")
  window = turtle.Screen()
  changeColor(donny, "coral")
  moveTurtle(donny, 100)
  window.exitonclick()

if __name__ == "__main__":
  main()