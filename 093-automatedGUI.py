from PIL import ImageGrab, ImageOps
from functools import partial
import pyautogui
import numpy as np
import time

URL = "https://elgoog.im/t-rex/"
DINO_IMAGE = r'.\day93\dino.png'

def imageGrab(left, top, width, height):
  # box in front of dino
  box = (left + width, top,
         left + (4*width), top + int(height / 2))
  # grab pixels
  image = ImageGrab.grab(box)
  # convert to grayscale
  image = ImageOps.grayscale(image)
  image.save(r'.\day93\test.png')
  # sum all pixelseeeeee
  a = np.array(image.getcolors())
  print(a.sum())
  return a.sum()

def main():
  ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

  #screenWidth, screenHeight = pyautogui.size()
  #currentMouseX, currentMouseY = pyautogui.position()

  dinoLeft, dinoTop, dinoWidth, dinoHeight = pyautogui.locateOnScreen(DINO_IMAGE, confidence=.9)
  pyautogui.click((dinoLeft, dinoTop))
  #pyautogui.moveTo(dinoLeft + dinoWidth, dinoTop)
  pyautogui.press('space')

  # Dino moves forward a bit when game starts
  dinoLeft += 30
  
  while True:
    if(imageGrab(dinoLeft, dinoTop, dinoWidth, dinoHeight) != 2767):
      pyautogui.press('space')
    time.sleep(0.1)

if __name__ == "__main__":
  main()