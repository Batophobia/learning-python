from PIL import ImageGrab, ImageOps
from functools import partial
import pyautogui

def imageGrab(left: int, top: int, width: int, height: int, grayscale: bool = False):
  box = (left, top, left + width, top + height)
  image = ImageGrab.grab(box)
  if grayscale:
    image = ImageOps.grayscale(image)
  return image

def multimonitor():
  ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

def getScreenSize():
  return pyautogui.size()

def getMousePos():
  return pyautogui.position()

def setMousePos(x: int, y: int):
  pyautogui.moveTo(x, y)

def findImage(img: str):
  return pyautogui.locateOnScreen(img, confidence=.9)

def clickIt(x=None, y=None, clicks=1, interval=0.0, button=pyautogui.PRIMARY, duration=0.0):
  pyautogui.click(x, y, clicks, interval, button, duration)