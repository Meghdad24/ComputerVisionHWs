import numpy as np
import cv2

I = cv2.imread('coins.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
G = cv2.GaussianBlur(G, (5,5), 0);

canny_high_threshold = 150
min_votes = 120 # minimum no. of votes to be considered as a circle
min_centre_distance = 15 # minimum distance between the centres of detected circles
resolution = 2 # resolution of parameters (centre, radius) relative to image resolution

while(True):
    I = cv2.imread('coins.jpg')
    
    circles = cv2.HoughCircles(G,cv2.HOUGH_GRADIENT,resolution,min_centre_distance,
                               param1=canny_high_threshold,
                               param2=min_votes,minRadius=0,maxRadius=100)

    
    for c in circles[0,:]:
        x = int(c[0]) # x coordinate of the centre
        y = int(c[1]) # y coordinate of the centre
        r = int(c[2])  # radius
        cv2.circle(I,(x,y), r, (0,255,0),2)    

    cv2.imshow("I",I)
    
    key = chr(cv2.waitKey(1) & 0xFF)
    
    if key == 'z':
        canny_high_threshold += 10
        print(canny_high_threshold)
    if key == 'x':
        canny_high_threshold -= 10
        print(canny_high_threshold)
    
        
    if key == '+':
        min_votes += 10
        print(min_votes)
    if key == '-':
        min_votes -= 10
        print(min_votes)
        
    
    if key == 'c':
        min_centre_distance += 1
        print(min_centre_distance)
    if key == 'v':
        min_centre_distance -= 1
        print(min_centre_distance)
        
        
    if key == 'b':
        resolution += 1
        print(resolution)
    if key == 'n':
        resolution -= 1
        print(resolution)   
        
        
    if key in ['q']:
        break



print(circles.shape)
    
n = len(circles[0,])
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(I,'There are %d coins!'%n,(400,40), font, 1,(255,0,0),2)

cv2.imshow("I",I)
cv2.waitKey(2000)
cv2.destroyAllWindows()

