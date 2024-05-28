# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:30:34 2024

@author: Pouria
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("pasargadae.jpg", cv2.IMREAD_GRAYSCALE)

levels = 256

f, axes = plt.subplots(2, 3)

axes[0,0].imshow(I, 'gray', vmin=0, vmax=255)
axes[0,0].axis('off')

axes[1,0].

# calculating histogram
def calc_hist(I, levels):
  hist = np.zeros(levels)
  for i in I:
      for x in i:
          hist[x] += 1 
  return hist.astype(np.uint8)

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

H = calc_hist(I, levels)
CDF = calc_cdf(H, levels)
print(CDF)