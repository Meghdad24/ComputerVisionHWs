# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 08:17:23 2024

@author: Pouria
"""

import numpy as np
import cv2

I = cv2.imread('damavand.jpg')
J = I.copy()

J[:,:,0] = J[:,:,2]
J[:,:,1] = J[:,:,2]

frame = np.arange(0,1.1,0.03)

for i in frame:
    print(i)
    K = cv2.addWeighted(I,i,J,1-i, 0)
    cv2.imshow("Anim", K)
    cv2.waitKey(500)
    
# for i in frame:
#     K = cv2.addWeighted(I,1-i,J,i, 0)
#     cv2.imshow("Anim", K)
#     cv2.waitKey(50)


cv2.destroyAllWindows()