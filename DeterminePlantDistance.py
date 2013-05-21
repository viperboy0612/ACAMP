import cv2
import numpy as np
import math

PI = 3.1415926

#Distance of plant (inches)
distance_of_plant = 28
#Camera Field Of View (degrees)
camera_FOV = 60
im = cv2.imread("Plant.jpg")
print "Resolution of Image :", im.shape[0], "x", im.shape[1]
cv2.namedWindow('window', cv2.CV_WINDOW_AUTOSIZE)
#Convert Image to gray and isolate darker colors
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
out = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)[1]
#Find the biggest blob and isolate it out
contours,hierarchy = cv2.findContours(out,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(out.shape, np.uint8)

largest_contour = 0  
i = 0
for contour in contours:
	if len(contour) > largest_contour:
		largest_contour = i
	i+=1
			
cv2.drawContours(mask,[contours[largest_contour]],-1,(100),-1)
cv2.imshow('window', mask)
yVals = []
for y in range(mask.shape[1]):
	for x in range(mask.shape[0]):
		if mask[x][y] != 0:
			yVals.append(y)
			break
yVals.sort()
print "Plant Distance(in) :", distance_of_plant
print "yHigh =",yVals[-1],"; yLow =",yVals[0]
plant_height_pixels = yVals[-1]-yVals[0]
print "Plant Height(pixels) :", plant_height_pixels
#Calculations to figure out height (inches) per pixel
screen_height_inches = 2*distance_of_plant*math.tan(camera_FOV*(PI/180)/2)
screen_height_pixels = im.shape[1]
height_per_pixel = screen_height_inches/screen_height_pixels
print "Plant Height(inches) :", plant_height_pixels*height_per_pixel

cv2.waitKey(0)
