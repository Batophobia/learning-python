import Automation.keyboardTools as keyboardTools
import Automation.mouseTools as mouseTools
import day97.commands as commands
from pynput.keyboard import Key, KeyCode

lastKey = None
ctrl = shift = alt = False
toRun = None
def checkKeys():
  global toRun

  if alt and shift and lastKey == Key.right:
    toRun = commands.wcoNext
  elif alt and shift and lastKey == Key.left:
    toRun = commands.wcoPrev
  elif ctrl and alt and shift and lastKey == Key.up:
    toRun = commands.wcoPlay
  #elif lastKey == KeyCode.from_char('a'):
  #  print("a")
  else:
    print(lastKey)

def on_press(key):
  global ctrl
  global shift
  global alt
  global lastKey

  if key == Key.ctrl_l or key == Key.ctrl_r:
    ctrl = True
  elif key == Key.shift or key == Key.shift_r:
    shift = True
  elif key == Key.alt_l or key == Key.alt_gr:
    alt = True
  elif(key != lastKey):
    lastKey = key
    checkKeys()

def on_release(key):
  global ctrl
  global shift
  global alt
  global lastKey
  global toRun

  if key == Key.ctrl_l or key == Key.ctrl_r:
    ctrl = False
  elif key == Key.shift or key == Key.shift_r:
    shift = False
  elif key == Key.alt_l or key == Key.alt_gr:
    alt = False
  elif key == Key.esc: # Stop listener
    return False
  else:
    lastKey = None

  if(not ctrl and not shift and not alt and lastKey == None and toRun != None):
    try:
      toRun()
    except:
      print("Failed to run function")
    toRun = None

def main():
  mouseTools.multimonitor()
  keyboardTools.setupListener(on_press, on_release)

if __name__ == "__main__":
  main()