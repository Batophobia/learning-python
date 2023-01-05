from tools import cls

NATO = {
  "a": "Alpha",
  "b": "Bravo",
  "c": "Charlie",
  "d": "Delta",
  "e": "Echo",
  "f": "Foxtrot",
  "g": "Golf",
  "h": "Hotel",
  "i": "India",
  "j": "Juliett",
  "k": "Kilo",
  "l": "Lima",
  "m": "Mike",
  "n": "November",
  "o": "Oscar",
  "p": "Papa",
  "q": "Quebec",
  "r": "Romeo",
  "s": "Sierra",
  "t": "Tango",
  "u": "Uniform",
  "v": "Victor",
  "w": "Whiskey",
  "x": "X-ray",
  "y": "Yankee",
  "z": "Zulu",
}

def nato(letter):
  if letter.isalpha():
    return NATO[letter]
  return letter

def main():
  cls()
  user = input("Enter word to translate: ")
  output = [nato(letter) for letter in user]
  print(' '.join(output))


if __name__ == "__main__":
  main()