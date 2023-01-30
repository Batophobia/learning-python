import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import numpy as np
from tools import updateTupleVal

IMG_W = 600
IMG_H = 600
NUM_COLORS = 10
FONT_NAME = "Courier"

window = TkinterDnD.Tk()
fileDrop = None
inputImage = None
img = None
colors = []
colorElems = []

def getImage(path):
  img = Image.open(path)
  img = img.resize((IMG_W, IMG_H))
  getColors(img)
  return ImageTk.PhotoImage(img)

def onDrop(event):
  global fileDrop
  global inputImage
  global img
  
  img = getImage(event.data)
  fileDrop.itemconfig(inputImage, image=img)

def getColors(image):
  global colors
  global colorElems
  colors = []
  imgColors = Image.Image.getcolors(image,360000)
  imgColors.sort(reverse=True)
  print(imgColors)
  for i in range(NUM_COLORS):
    tempLabel = colorElems[i]["label"]
    tempButton = colorElems[i]["button"]
    if(i >= len(imgColors)):
      tempLabel.config(text="", fg="#FFFFFF")
      tempButton.config(text="", bg="#FFFFFF")
    else:
      #   Greyscale images seem to return single-number colors.
      #   Awaiting info on how those might translate:
      #   https://stackoverflow.com/questions/75287239/how-does-a-single-number-value-work-for-coloring
      if type(imgColors[i][1]) == int:
        if imgColors[i][1] == 0:
          imgColors[i] = updateTupleVal(imgColors[i], 1, (0,0,0))
        elif imgColors[i][1] == 1:
          imgColors[i] = updateTupleVal(imgColors[i], 1, (255,255,255))
        else:
          val = int(255 * imgColors[i][1] / 10)
          imgColors[i] = updateTupleVal(imgColors[i], 1, (val, val, val))
      colors.append(imgColors[i][1])
      hexVal = '#%02x%02x%02x' % imgColors[i][1][0:3] # Get first 3, ignore alpha
      tempLabel.config(text=hexVal, fg=hexVal)
      tempButton.config(text=hexVal, command = lambda hexVal=hexVal: copyVal(hexVal), bg=hexVal)

def copyVal(hexVal):
  window.clipboard_clear()
  window.clipboard_append(hexVal)

def main():
  global window
  global fileDrop
  global inputImage
  global img
  global colors

  window.title("Color Palette")
  window.config(padx=20, pady=20)
  
  fileDrop = tk.Canvas(window, bg='white', width = IMG_W, height = IMG_H)
  fileDrop.drop_target_register(DND_FILES)
  fileDrop.dnd_bind('<<Drop>>', onDrop)
  fileDrop.grid(column=0, row=0, rowspan=10)

  for i in range(NUM_COLORS):
    tempLabel = tk.Label(text = "COLOR", font = (FONT_NAME, 20, "bold"))
    tempLabel.grid(column=1, row=i)
    tempButton = tk.Button(text = f"Color {i+1}", highlightthickness=0)
    tempButton.grid(column=2, row=i)
    colorElems.append({"label": tempLabel, "button": tempButton})

  img = getImage(r".\day84\test.png")
  inputImage = fileDrop.create_image((0, 0), anchor=tk.NW, image=img)
  
  window.mainloop()


if __name__ == "__main__":
  main()