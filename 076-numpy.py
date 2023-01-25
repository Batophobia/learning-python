import numpy as np
import matplotlib.pyplot as plt
from scipy.datasets import face
from PIL import Image

def simplePlot():
  x = np.linspace(0,100,num=9)
  y = np.linspace(start=-3,stop=3,num=9)
  plt.plot(x,y)
  plt.show()

def arrMath():
  a1 = np.array([[1,3], [0,1],[6,2],[9,7]])
  a2 = np.array([[4,1,3],[5,8,5]])
  return np.matmul(a1,a2)

def main():
  FILENAME = "./day76/yummy_macarons.jpg"
  img = np.array(Image.open(FILENAME))
  #img = face()
  arrRGB = img/255
  greyscalar = np.array([0.2126, 0.7152, 0.0722])
  arrBW = arrRGB @ greyscalar
  #              ^ np.matmul(arrRGB, greyscalar)
  #plt.imshow(arrBW, cmap="gray")
  plt.imshow(np.flip(arrBW), cmap="gray")
  #plt.imshow(np.rot90(arrBW), cmap="gray")
  #plt.imshow(255 - img)
  #plt.imshow(img)
  plt.show()
  
if __name__ == "__main__":
  main()