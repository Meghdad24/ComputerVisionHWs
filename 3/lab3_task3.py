import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("pasargadae.jpg", cv2.IMREAD_GRAYSCALE)

levels = 256

# calculating histogram
def calc_hist(I, levels):
  hist = np.zeros(levels)
  for i in I:
      for x in i:
          hist[x] += 1 
  return hist.astype(np.uint64)


# calculating CDF
def calc_cdf(hist, levels):
  cdf = np.zeros_like(hist).astype(np.uint64())
  i = 0
  for n in hist:
      if i == 0:
          cdf[0] = hist[0]
      else:
          cdf[i] = cdf[i-1] + hist[i]
      i += 1
  return cdf

hist = calc_hist(I, levels)
cdf = calc_cdf(hist, levels)

# normalize CDF
cdf = cdf.astype(float)
maxNum = cdf[255]
for i in range(0,256):
    cdf[i] = cdf[i] / maxNum
    pass

# mapping
mapping = cdf * 255

# replace intensity
equalized_image = []
for column in I:
    columnn = []
    for n in column:
        columnn.append(mapping[n])
    equalized_image.append(columnn)
equalized_image = np.array(equalized_image).astype(np.uint8)

equalized_image_hist = calc_hist(equalized_image, levels)
equalized_image_cdf = calc_cdf(equalized_image_hist, levels)

fig = plt.figure(figsize= (16, 8))
fig.add_subplot(2,3,1)
plt.imshow(I, cmap='gray')
plt.title('pasargadae')
plt.axis('off')

fig.add_subplot(2,3,2)
plt.plot(hist)
plt.title('Source histogram')

fig.add_subplot(2,3,3)
plt.plot(cdf)
plt.title('Source CDF')

fig.add_subplot(2,3,4)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized image')
plt.axis('off')

fig.add_subplot(2,3,5)
plt.plot(equalized_image_hist)
plt.title('Equalized histogram')


fig.add_subplot(2,3,6)
plt.plot(equalized_image_cdf)
plt.title('Equalized CDF')

plt.show()