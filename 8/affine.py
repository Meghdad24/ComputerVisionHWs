import cv2
import numpy as np

I = cv2.imread('karimi.jpg')


tx = 0
ty = 0

t = np.array([[tx],
              [ty]], dtype=np.float32)

A = np.array([[1.3, 0],
              [0, 1.2]], dtype=np.float32)




M = np.hstack([A,t])

output_size = (I.shape[1], I.shape[0])
J = cv2.warpAffine(I,M,  output_size)

cv2.imshow('I',I)
cv2.waitKey(0)
cv2.imshow('J',J)
cv2.waitKey(0)

cv2.destroyAllWindows()
