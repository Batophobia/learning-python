import tkinter

def setEntry(elem: tkinter.Entry, val):
  elem.delete(0, tkinter.END)
  elem.insert(0, val)