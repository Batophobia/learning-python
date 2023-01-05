from tkinter import *
from tools import isNumber
from guitools import setEntry

def main():
  def CtoF(temp):
    return temp * 9 / 5 + 32

  def FtoC(temp):
    return (temp - 32) * 5 / 9

  def onButtonClick():
    val1 = inpt1.get()
    val2 = inpt2.get()
    if isNumber(val1):
      setEntry(inpt2, CtoF(float(val1)))
    elif isNumber(val2):
      setEntry(inpt1, FtoC(float(val2)))
  
  window = Tk()
  window.title("Unit Converter")
  #window.minsize(width = 500, height = 400)
  window.config(padx=10, pady=10)

  label = Label(text = "Unit Converter", font = ("Arial", 24, "bold"))
  label.grid(column=0, columnspan=2, row=0, padx=10, pady=10)
  
  unit1 = Label(text = "Celcius", font = ("Arial", 14, "normal"))
  unit1.grid(column=0, row=1)
  
  unit2 = Label(text = "Farenheit", font = ("Arial", 14, "normal"))
  unit2.grid(column=0, row=2)
  
  inpt1 = Entry()
  inpt1.grid(column=1, row=1)

  inpt2 = Entry()
  inpt2.grid(column=1, row=2)

  button = Button(text = "Convert", command = onButtonClick)
  button.grid(column=0, columnspan=2, row=3, pady=10)
  
  window.mainloop()


if __name__ == "__main__":
  main()