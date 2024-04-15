# from PIL import Image

# IMG_W = 600
# IMG_H = 600
# image = Image.open(r"D:\tmp\dpOfh.png")
# image = image.resize((IMG_W, IMG_H))
# imgColors = Image.Image.getcolors(image,360000)
# imgColors.sort(reverse=True)
# print(imgColors)

import random
OUTFILE="./output.txt"

def run():
  num = random.randint(0,10)
  with open(OUTFILE, mode="w") as file:
      file.write(str(num))

def main():
  run()

if __name__ == '__main__':
  main()