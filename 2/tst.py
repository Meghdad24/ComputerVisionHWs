# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 07:18:24 2024

@author: Pouria
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# I = cv2.imread('masoleh_gray.jpg', cv2.IMREAD_UNCHANGED)
# cv2.imshow('Masoleh Village', I)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()
# I = cv2.imread('masoleh.jpg')
# I = cv2.imread('masoleh.jpg')
# cv2.imshow('Masoleh', I)
# a = cv2.waitKey() # display the image for 10 seconds
# print(a)
# cv2.destroyAllWindows()
# plt.imshow(I)
# plt.show()

I = cv2.imread('masoleh.jpg')
# notice that OpenCV uses BGR instead of RGB!
B = I[:,:,0]
G = I[:,:,1]
R = I[:,:,2]
cv2.imshow('win1',I)
while 1:
    k = cv2.waitKey()
    if k == ord('o'):
        cv2.imshow('win1',I)
    elif k == ord('b'):
        cv2.imshow('win1',B)
    elif k == ord('g'):
        cv2.imshow('win1',G)
    elif k == ord('r'):
        cv2.imshow('win1',R)
    elif k == ord('q'):
        cv2.destroyAllWindows()
        break
    
B = np.zeros(I.shape, dtype=np.uint8)
print(B.shape)
B[:,:,0] = I[:,:,0].copy()
cv2.imshow('1',B)
cv2.waitKey()
cv2.destroyAllWindows()