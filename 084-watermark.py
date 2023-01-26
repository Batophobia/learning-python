import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

IMG_W = 600
IMG_H = 600
window = TkinterDnD.Tk()
fileDrop = None
inputImage = None
img = None

def getImage(path):
  img = Image.open(path)
  img = img.resize((IMG_W, IMG_H))
  return ImageTk.PhotoImage(img)

def onDrop(event):
  global fileDrop
  global inputImage
  global img
  
  img = getImage(event.data)
  fileDrop.itemconfig(inputImage, image=img)

def main():
  global window
  global fileDrop
  global inputImage
  global img

  window.title("Watermarker")
  window.config(padx=20, pady=20)
  
  fileDrop = tk.Canvas(window, bg='white', width = IMG_W, height = IMG_H)
  fileDrop.drop_target_register(DND_FILES)
  fileDrop.dnd_bind('<<Drop>>', onDrop)
  fileDrop.pack()

  img = getImage("./day84/test.png")
  inputImage = fileDrop.create_image((0, 0), anchor=tk.NW, image=img)
  
  fileDrop.create_text((IMG_W / 2, IMG_H / 2), text='--WATERMARK--', font=('Times', 60), angle=45)

  window.mainloop()


if __name__ == "__main__":
  main()