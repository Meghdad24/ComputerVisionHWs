import numpy as np
import cv2

def generate_circle_array(size):
    arr = np.zeros((size, size),np.uint8)
    
    center = size // 2
    
    radius = min(center, size - center - 1)
    
    for i in range(size):
        for j in range(size):
            if (i - center) ** 2 + (j - center) ** 2 <= radius ** 2:
                arr[i, j] = 1
                
    return arr

I = cv2.imread('beans.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

ret, T = cv2.threshold(G,127,255,cv2.THRESH_BINARY)

cv2.imshow('Thresholded', T)
cv2.waitKey(0) # press any key to continue...

## erosion 
kernel = np.ones((20,20),np.uint8)
T = cv2.erode(T,kernel)
cv2.imshow('After Erosion', T)
cv2.waitKey(0) # press any key to continue...

# kernel = np.array([[0,0,0,1,0,0,0],
#                    [0,0,1,1,1,0,0],
#                    [0,1,1,1,1,1,0],
#                    [1,1,1,1,1,1,1],
#                    [0,1,1,1,1,1,0],
#                    [0,0,1,1,1,0,0],
#                    [0,0,0,1,0,0,0]],np.uint8)

kernel = generate_circle_array(16)


T = cv2.dilate(T,kernel)
cv2.imshow('After Erosion', T)
cv2.waitKey(0)

n,C = cv2.connectedComponents(T);

font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(T,'There are %d beans!'%(n-1),(20,40), font, 1, 255,2)
cv2.imshow('Num', T)
cv2.waitKey(0)
cv2.destroyAllWindows()


