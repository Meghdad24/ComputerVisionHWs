import cv2
import numpy as np

I = cv2.imread('karimi.jpg')

tx = 0
ty = 0

th =  45 # angle of rotation (degrees)
th *= np.pi / 180 # convert to radians

s = float(input()) # scale factor

M = np.array([[s*np.cos(th),-s*np.sin(th),tx],
              [s*np.sin(th), s*np.cos(th),ty]])

output_size = (I.shape[1]*int(s), I.shape[0]*int(s))
J = cv2.warpAffine(I,M,  output_size)

cv2.imshow('I',I)
cv2.waitKey(0)

cv2.imshow('J',J)
cv2.waitKey(0)

cv2.destroyAllWindows()