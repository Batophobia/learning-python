import os.path
import time
from pathlib import Path
from day81 import Morse

def main():
  INPUT_FILE = "day81/input.txt"
  OUTPUT_PATH = "day81/output/"
  if(os.path.isfile(INPUT_FILE)):
    with open(INPUT_FILE) as file:
      user = file.read()
  else:
    user = input("Enter message to translate:\n")
  saveLoc = time.strftime("%Y%m%d-%H%M%S")
  Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)
  with open(f"{OUTPUT_PATH}{saveLoc}.test.ignore", mode="w") as file:
    file.write(Morse.encode(user))


if __name__ == "__main__":
  main()