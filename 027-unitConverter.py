from tkinter import *

def main():
  def buttonClick():
    label.config(text=inpt.get())
  
  window = Tk()
  window.title("Unit Converter")
  window.minsize(width = 500, height = 400)

  label = Label(text = "Things be workin'", font = ("Arial", 24, "italic"))
  label.pack(side="top")
  
  button = Button(text = "I'm a button", command = buttonClick)
  button.pack(side="bottom")

  inpt = Entry(width = 10)
  inpt.pack(side="top")
  txtbox = Text(height = 3, width=10)
  txtbox.pack(side="left")
  
  numBox = Spinbox(from_=10, to=100, width=5)
  numBox.pack(side="top")

  scroll = Scale(from_= 0, to=100)
  scroll.pack(side="right")

  isChecked = IntVar()
  check = Checkbutton(text="Am I checked?", variable=isChecked)
  check.pack(side="bottom")

  radioSelect = IntVar()
  radios = []
  radios.append(Radiobutton(text="TOP TEXT", variable=radioSelect, value=1))
  radios.append(Radiobutton(text="BOTTOM TEXT", variable=radioSelect, value=2))
  for radio in radios:
    radio.pack(side="top")

  def onSelect(event):
    print(multi.get(multi.curselection()))

  multi = Listbox(height = 3)
  fruits = ["Apple","Grape","Orange","Pineapple"]
  for itm in fruits:
    multi.insert(fruits.index(itm), itm)
  multi.bind("<<ListboxSelect>>", onSelect)
  multi.pack(side="bottom")

  window.mainloop()


if __name__ == "__main__":
  main()