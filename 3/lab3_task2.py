import cv2
import numpy as np
from matplotlib import pyplot as plt


def calc_hist(I):
  hist = np.zeros(256)
  for i in I:
      for x in i:
          hist[x] += 1 
  return hist.astype(np.uint64)

def autoA(hist):
    a = 0
    for i in hist:
        if i > max(hist)//5:
            break
        a +=1
    return a

def autoB(hist):
    b = 255
    for i in np.flip(hist):
        if i > max(hist)//5:
            break
        b -=1
    return b
    
# fname = 'crayfish.jpg'
# fname = 'office.jpg'
# fname = 'map.jpg'
# fname = 'train.jpg'
fname = 'branches.jpg'
# fname = 'terrain.jpg'
# fname = "pasargadae.jpg"

I = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

f, axes = plt.subplots(2, 3)

axes[0,0].imshow(I, 'gray', vmin=0, vmax=255)
axes[0,0].axis('off')

axes[1,0].hist(I.ravel(),255,[0,255]);

a = autoA(calc_hist(I))
b = autoB(calc_hist(I))

# a = 100
# b = 180

# a = 150
# b = 200

# a = 150
# b = 200

# a = 80
# b = 230

# a = 150
# b = 220

# a = 120
# b = 220

J = (I-a) * 255.0 / (b-a)
J[J < 0] = 0
J[J > 255] = 255
J = J.astype(np.uint8)

axes[0,1].imshow(J, 'gray', vmin=0, vmax=255)
axes[1,1].hist(J.ravel(),255,[0,255]);

K = cv2.equalizeHist(I)

axes[0,2].imshow(K, 'gray', vmin=0, vmax=255)
axes[1,2].hist(K.ravel(),255,[0,255]);

plt.show()
