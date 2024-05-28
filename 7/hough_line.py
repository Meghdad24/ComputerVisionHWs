import numpy as np
import cv2

def draw_line(I,rho,theta):
    "draws a line in image 'I' given 'rho' and 'theta'"
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    
    cv2.line(I,(x1,y1),(x2,y2),(0,0,255),1)

    
I = cv2.imread('highway.jpg')

G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) # -> grayscale

l = 100
h = 200

min_votes = 160 # mininum votes to be considered a line
distance_resolution = 1 # 1 pixel: resolution of the parameter "rho" (distance to origin)
a = 180
angle_resolution = np.pi/5 # pi/180 radians: resolution (bin size) of the parameter "theta" 


while(True):
    I = cv2.imread('highway.jpg')
    
    E = cv2.Canny(G,l,h) # find the edges
    
    L = cv2.HoughLines(E,distance_resolution,angle_resolution,min_votes)
    
    # draw the lines 
    for [[rho,theta]] in L:
        draw_line(I,rho,theta)

    cv2.imshow("I",I)
    cv2.imshow("E",E)
    
    key = chr(cv2.waitKey(1) & 0xFF)
    
        
    if key == '+':
        min_votes += 10
        print(min_votes)
    if key == '-':
        min_votes -= 10
        print(min_votes)
        
    if key == 'z':
        distance_resolution += 1
        print(distance_resolution)
    if key == 'x':
        distance_resolution -= 1
        print(distance_resolution)
    
    
    if key == 'c':
        a += 5
        angle_resolution = np.pi/a
        print(angle_resolution, a)
    if key == 'v':
        a -= 5
        angle_resolution = np.pi/a
        print(angle_resolution, a)
    
        
    if key == 'a':
        l += 5
        print(f"l = {l}")
    if key == 's':
        l -= 5
        print(f"l = {l}")
    
    
    if key == 'q':
        h += 5
        print(f"h = {h}")
    if key == 'w':
        h -= 5
        print(f"h = {h}")
    
    
    if key in ['p']:
        break

cv2.destroyAllWindows()

