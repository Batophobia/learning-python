import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
special = "!_=+-#^&*()\|/?,.:;[]"

l = int(input("How many lowercase? "))
u = int(input("How many UPPERCASE? "))
n = int(input("How many numbers? "))
s = int(input("How many special characters? "))

output = ""
while l > 0:
  l -= 1
  output += random.choice(lower)
while u > 0:
  u -= 1
  output += random.choice(upper)
while n > 0:
  n -= 1
  output += random.choice(nums)
while s > 0:
  s -= 1
  output += random.choice(special)

arr = list(output)
random.shuffle(arr)
output = ''.join(arr)

print(output)