import cv2
import numpy as np
import math

#values for real plant
#hueL, hueH = 35, 59
#satL, satH = 72, 177
#valL, valH = 81, 171


def getCameraData():
	#values for fake plant
	hueL, hueH = 28, 90
	satL, satH = 30, 75
	valL, valH = 0, 65

	DEBUG = 0
	
	min_height = 4
	#Height of Camera (inches)
	height_of_camera = 7
	#Distance of plant (inches)
	distance_of_plant = 22
	#Camera Field Of View (degrees)
	camera_FOV = 52
	#im = cv2.imread("Images/Webcam.png")
	camera = cv2.VideoCapture(0)
	for i in xrange(30):
		retval, im = camera.read()
	if DEBUG:
		cv2.namedWindow('window', cv2.CV_WINDOW_AUTOSIZE)
		#Show Original Image
		cv2.imshow('window', im)
		cv2.waitKey(0)
	hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
	COLOR_MIN = np.array([hueL, satL, valL], np.uint8)
	COLOR_MAX = np.array([hueH, satH, valH], np.uint8)
	filtered_hsv = cv2.inRange(im, COLOR_MIN, COLOR_MAX)
	if DEBUG:
		cv2.imshow('window', filtered_hsv)	
		cv2.waitKey(0)
	contours,hierarchy = cv2.findContours(filtered_hsv,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	mask = np.zeros(filtered_hsv.shape, np.uint8)
	largest_contour = 0  
	i = 0
	for contour in contours:
		if len(contour) > largest_contour:
			largest_contour = i
		i+=1
			
	cv2.drawContours(mask,[contours[largest_contour-1]],-1,(255),-1)
	if DEBUG:
		cv2.imshow('window', mask)
		cv2.waitKey(0)	
	#Determine Plant Pixel Height
	#By grabbing all the values that includes the plant
	#LargestValue - SmallestValue = Plant Height (Pixels)
	yVals = []
	maskT = cv2.transpose(mask)
	for y in range(maskT.shape[0]):	
		if any(maskT[y]):
			yVals.append(y)
	yVals.sort()
	plant_height_pixels = yVals[-1]-yVals[0]
	screen_height_inches = 2*distance_of_plant*math.tan(camera_FOV*(math.pi/180)/2)
	screen_height_pixels = im.shape[1]
	height_per_pixel = screen_height_inches/screen_height_pixels
	plant_height_inches = plant_height_pixels*height_per_pixel
	plant_height_millimeters = (plant_height_inches+min_height)*25.4
	if DEBUG:
		#Print out calculations
		#print "Plant Distance(in) :", distance_of_plant
		print "yHigh =",yVals[-1],"; yLow =",yVals[0]
		#print "Plant Height(pixels) :", plant_height_pixels
		#Calculations to figure out height (inches) per pixel
		print "screen_height_inches",screen_height_inches
		print "shape", im.shape[0], im.shape[1]
		print "height_per_pixel", height_per_pixel
		print "Plant Height(inches) :", plant_height_inches+min_height

	cv2.destroyAllWindows()
	return plant_height_millimeters
