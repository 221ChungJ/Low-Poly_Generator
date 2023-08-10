import cv2 
import scipy as sp
import numpy as np
import math
from scipy.spatial import Delaunay
from numpy import random 

def averageValues(i, j, inputImage):
    num = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
                num = num + inputImage[x][y] 
    return num

highThreshholdEdges = 110 #Upper bound
lowThreshholdEdges = 100 #Lower bound
threshholdNodes = 765 # Minimum Number of Pixels in 3x3 Window
numPoints = 11000 # Number of points that make up the triangle
scale_percent = 100 # Percent of original size

imageName = "banner.jpg" #Image file 

imgOrg = cv2.imread(imageName)
width = int(imgOrg.shape[1] * scale_percent / 100)
height = int(imgOrg.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(imgOrg, dim, interpolation = cv2.INTER_AREA)
img2 = cv2.resize(imgOrg, dim, interpolation = cv2.INTER_AREA)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
img_edges = cv2.Canny(img_blur,lowThreshholdEdges,highThreshholdEdges)
#status = cv2.imwrite('LowPolyGenerator/img_edges.png',img_edges)

h, w = len(img_edges), len(img_edges[0])

'''
cv2.imshow('Image Edges', img_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

points = []
largest = (0,h)

for i in range(1,h-1):
    for j in range(1, w-1):
        if img_edges[i][j] == 255:
            points.append((int(j), int(i)))


NodeList = []
for z in range(numPoints):
    x = random.randint(len(points))
    NodeList.append(points[x])
    points.pop(x)

NodeList.append((0,0))
NodeList.append((w,h))
NodeList.append((0,h))
NodeList.append((w,0))
NodeList.append((w,200))

for i in NodeList:
    cv2.circle(img2, (i[0],i[1]), 3, (0,0,255), -1)

newList = np.array(NodeList)
tri = Delaunay(newList)

blank_image = np.zeros((h,w,3), np.uint8)

for ia, ib, ic in tri.vertices:
    ia, ib, ic = NodeList[ia], NodeList[ib], NodeList[ic]

    x1, x2, x3 = ia[0], ib[0], ic[0]
    y1, y2, y3 = ia[1], ib[1], ic[1]

    xc = (x1+x2+x3)//3 
    yc = (y1+y2+y3)//3   
    colors1 = img[yc][xc]
    colors2 = (int(colors1[0]), int(colors1[1]), int(colors1[2]))
    
    trianglePoints = [ia, ib, ic]

    cv2.drawContours(blank_image, np.array([trianglePoints]), 0, colors2, -1)

    
    cv2.line(img2, (ia[0], ia[1]) , (ib[0], ib[1]), (256,256,256))
    cv2.line(img2, (ib[0], ib[1]) , (ic[0], ic[1]), (256,256,256))
    cv2.line(img2, (ia[0], ia[1]) , (ic[0], ic[1]), (256,256,256))
    

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Image Edges', img_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Final Image', blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

status = cv2.imwrite('final_image.png',blank_image)