from PIL import Image

IMG_W = 600
IMG_H = 600
image = Image.open(r"D:\tmp\dpOfh.png")
image = image.resize((IMG_W, IMG_H))
imgColors = Image.Image.getcolors(image,360000)
imgColors.sort(reverse=True)
print(imgColors)