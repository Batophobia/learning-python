runAgain = True

def cipher(message, shift=13):
  output = ""
  for letter in message:
    if letter == " ":
      output += letter
    else:
      output += chr((ord(letter) - 97 + shift) % 26 + 97)
  print(output)

while runAgain:
  mode = input("Would you like to [encode] or [decode]?\n").lower()
  match mode:
    case "decode":
      mode = "decode"
    case "decrypt":
      mode = "decode"
    case "d":
      mode = "decode"
    case _:
      mode = "encode"
  shift = int(input("What is the shift amount? "))
  user = input(f"Enter the message to {mode}.\n").lower()
  if mode == "decode":
    cipher(user, shift)
  else:
    cipher(user, -shift)
  
  user = input("Would you like to run again (Y/n)? ").lower()
  if user != "y":
    runAgain = False