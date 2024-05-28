import cv2
import numpy as np

I = cv2.imread('polygons.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('corners',G)
cv2.waitKey(0)

ret, T = cv2.threshold(G,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow('corners',T)
cv2.waitKey(0)

nc1,CC1 = cv2.connectedComponents(T)

for k in range(1,nc1):

    Ck = np.zeros(T.shape, dtype=np.float32)
    Ck[CC1 == k] = 1;
    Ck = cv2.GaussianBlur(Ck,(5,5),0)
    Cko = cv2.cvtColor(Ck,cv2.COLOR_GRAY2BGR)

    # Now, apply corner detection on Ck
    G = np.float32(Ck)
    window_size = 7
    soble_kernel_size  = 3 # kernel size for gradients
    alpha = 0.04
    H = cv2.cornerHarris(G,window_size,soble_kernel_size,alpha)
    
    # normalize C so that the maximum value is 1
    H = H / H.max()
    
    C = np.uint8(H > 0.001) * 255
    cv2.imshow('corners',C)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    
    ## connected components
    nc,CC = cv2.connectedComponents(C);
    
    # to count the number of corners we count the number
    # of nonzero elements of C (wrong way to count corners!)
    # n = np.count_nonzero(C)
    n = nc -1 
    
    # Show corners as red pixels in the original image
    Cko[C != 0] = [0,0,255]
    
    cv2.imshow('corners',Cko)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    
    font = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(Cko,'There are %d vertices!'%(n),(20,30), font, 1,(0,0,255),1)

    
    cv2.imshow('corners',Cko)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


