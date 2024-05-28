import numpy as np
import cv2

I = cv2.imread('sign.jpg')

p1 = (135,105)
p2 = (331,143)
p3 = (356,292)
p4 = (136,290)

points1 = np.array([p1,p2,p3,p4], dtype=np.float32)

n = 480
m = 320
output_size = (n,m)

p5 = (0,0)
p6 = (n,0)
p7 = (n,m)
p8 = (0,m)
points2 = np.array([p5,p6,p7,p8], dtype=np.float32)


# mark corners of the plate in image I
for i in range(4):
    cv2.circle(I, (int(points1[i,0]), int(points1[i,1])), 2, [0,0,255],2)


H = cv2.getPerspectiveTransform(points1, points2)

J = cv2.warpPerspective(I,H,  output_size)

cv2.imshow('I', I);
cv2.waitKey(0)

cv2.imshow('J', J);
cv2.waitKey(0)

cv2.destroyAllWindows()