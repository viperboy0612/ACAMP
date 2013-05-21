import cv2
import numpy as np
import math

whiteThreshold = 100

PI = 3.1415926

#def whiteFilter(im):
#	for row in range(480):
#		for col in range(640):
#			if im[row,col,0] > whiteThreshold and im[row,col,1] > whiteThreshold and im[row,col,2] > whiteThreshold:
#				for i in range(3):
#					im[row,col,i] = 0
#	return im


#Distance of plant (inches)
distance_of_plant = 28
#Camera Field Of View (degrees)
camera_FOV = 60
im = cv2.imread("Plant.jpg")
print "Resolution of Image :", im.shape[0], "x", im.shape[1]
cv2.namedWindow('window', cv2.CV_WINDOW_AUTOSIZE)
#Show Original Image
cv2.imshow('window', im)
cv2.waitKey(0)
#removeWhite
print "noWhite"
print type(im)
COLOR_MIN = np.array([whiteThreshold, whiteThreshold, whiteThreshold], np.uint8)
COLOR_MAX = np.array([255, 255, 255], np.uint8)
print type((whiteThreshold, whiteThreshold, whiteThreshold))
no_white = cv2.inRange(im, COLOR_MIN, COLOR_MAX)
#no_white = whiteFilter(im)
cv2.imshow('window', no_white)
cv2.waitKey(0)
#Convert Image to gray and isolate darker colors
#gray = cv2.cvtColor(no_white, cv2.COLOR_BGR2GRAY)
#cv2.imshow('window', gray)
#cv2.waitKey(0)
#Isolate out darker colors
#out = cv2.threshold(no_white, 1, 255, cv2.THRESH_BINARY_INV)[1]
#cv2.imshow('window', out)
#cv2.waitKey(0)
#Find the biggest blob and isolate it out
contours,hierarchy = cv2.findContours(no_white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(no_white.shape, np.uint8)
largest_contour = 0  
i = 0
for contour in contours:
	if len(contour) > largest_contour:
		largest_contour = i
	i+=1
			
cv2.drawContours(mask,[contours[largest_contour]],-1,(255),-1)
cv2.imshow('window', mask)

#Determine Plant Pixel Height
#By grabbing all the values that includes the plant
#LargestValue - SmallestValue = Plant Height (Pixels)
yVals = []
maskT = cv2.transpose(mask)
for y in range(mask.shape[1]):	
	for x in range(mask.shape[0]):
		if mask[x][y] != 0:
			yVals.append(y)
			break
yVals.sort()

#Print out calculations
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
cv2.destroyAllWindows()
