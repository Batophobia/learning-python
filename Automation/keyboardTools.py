import pynput.keyboard as pynput

def getKeyVal(key: pynput.Key):
  return str(key)

def on_press(key, func):
  func(key)

def on_release(key, func):
  return func(key)

def setupListener(onpress, onrelease):
  # Collect events until released
  with pynput.Listener(
    on_press = lambda key: on_press(key, onpress),
    on_release = lambda key: on_release(key, onrelease)
  ) as listener:
    listener.join()