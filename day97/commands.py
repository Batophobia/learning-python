from Automation.keyboardTools import setupListener
import Automation.mouseTools as mouseTools

def wcoNext():
  x, y, w, h = mouseTools.findImage(r'./day97/wcoNext.png')
  #mouseTools.setMousePos(x - 30, y + 30)
  mouseTools.clickIt(x - 30, y + 30)

def wcoPrev():
  x, y, w, h = mouseTools.findImage(r'./day97/wcoPrev.png')
  mouseTools.clickIt(x + 30, y + 30)

def wcoPlay():
  oldPos = mouseTools.getMousePos()
  try:
    x, y, w, h = mouseTools.findImage(r'./day97/wcoPlay.png')
    mouseTools.clickIt(x, y)
  except TypeError:
    print("Could not find play button")
  mouseTools.setMousePos(oldPos.x, oldPos.y)

def on_release(key):
  print('{0} release'.format(key))
  if key == Key.esc: # Stop listener
    return False

def main():
  setupListener(on_press, on_release)
  mouseTools.multimonitor()

if __name__ == "__main__":
  main()