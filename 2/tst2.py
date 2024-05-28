# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 07:42:50 2024

@author: Pouria
"""

import cv2
import numpy as np

I = cv2.imread('damavand.jpg')
J = cv2.imread('eram.jpg')

# print(I.shape)

# print(J.shape)

# k = I.copy()
# K = I.copy()
# k[::2,::2,:] = J[::2,::2,:]
# K = I//2+J//2
# Ka = 255-I
# Kb = 255-J

frame = np.arange(-500,500,10)

# for i in frame:
# print(i)
K = cv2.addWeighted(I,1,J,1,-100)
cv2.imshow("Anim", K)
cv2.waitKey()
    
# for i in frame:
#     K = cv2.addWeighted(I,1-i,J,i, 0.2)
#     cv2.imshow("Anim", K)
#     cv2.waitKey(50)


# K = cv2.addWeighted(I,i,J,j, 0)
# cv2.imshow("Blending", K)
# cv2.waitKey()
cv2.destroyAllWindows()



# K = cv2.addWeighted(I,0.1,J,0.9, 0)
# cv2.imshow("Blending", K)
# cv2.waitKey()
# cv2.destroyAllWindows()

# K = cv2.addWeighted(I,0.3,J,0.7, 0)
# cv2.imshow("Blending", K)
# cv2.waitKey()
# cv2.destroyAllWindows()