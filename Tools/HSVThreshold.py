import cv2
import sys
import numpy as np

hueL, hueH, satL, satH, valL, valH = 0,0,0,0,0,0

def hueLchange(value):
	global hueL
	hueL = value
	if hueL > hueH:
		print "Invalid Value: hueL > hueH"
	else:
		updateImage()

def hueHchange(value):
	global hueH
	hueH = value
	if hueH < hueL:
		print "Invalid Value: hueH > hueL"
	else:
		updateImage()
	
def saturationLchange(value):
	global satL
	satL = value
	if satL > satH:
		print "Invalid Value: satL > satH"
	else:
		updateImage()

def saturationHchange(value):
	global satH
	satH = value
	if satH < satL:
		print "Invalid Value: satH > satL"
	else:
		updateImage()

def valueLchange(value):
	global valL
	valL = value
	if valL > valH:
		print "Invalid Value: valL > valH"
	else:
		updateImage()

def valueHchange(value):
	global valH
	valH = value
	if valH < valL:
		print "Invalid Value: valH > valL"
	else:
		updateImage()


def updateImage():
	print "Updating Image"
        COLOR_MIN = np.array([hueL, 0, 0], np.uint8)
        COLOR_MAX = np.array([hueH, 255, 255], np.uint8)
        filtered_hsv = cv2.inRange(img, COLOR_MIN, COLOR_MAX)
        cv2.imshow('hsv', filtered_hsv)
        COLOR_MIN = np.array([hueL, satL, 0], np.uint8)
        COLOR_MAX = np.array([hueH, satH, 255], np.uint8)
	filtered_sat = cv2.inRange(img, COLOR_MIN, COLOR_MAX)
	cv2.imshow('saturation', filtered_sat)
        COLOR_MIN = np.array([hueL, satL, valL], np.uint8)
        COLOR_MAX = np.array([hueH, satH, valH], np.uint8)
	filtered_val = cv2.inRange(img, COLOR_MIN, COLOR_MAX)
	cv2.imshow('value', filtered_val)

img = cv2.imread("../Images/Webcam.png",cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file
cv2.namedWindow('original')        ## create original for display
cv2.namedWindow('originalhsv')
cv2.namedWindow('hsv')
cv2.namedWindow('saturation')
cv2.namedWindow('value')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('original',img)         ## Show image in the original
cv2.imshow('hsv', hsv)
cv2.imshow('saturation', hsv)
cv2.imshow('value', hsv)
cv2.imshow('originalhsv', hsv)
cv2.createTrackbar("Hue Low", "original", 0, 179, hueLchange)
cv2.createTrackbar("Hue High", "original", 0, 179, hueHchange)

cv2.createTrackbar("Saturation Low", "original", 0, 255, saturationLchange)
cv2.createTrackbar("Saturation High", "original", 0, 255, saturationHchange)

cv2.createTrackbar("Value Low", "original", 0, 255, valueLchange)
cv2.createTrackbar("Value High", "original", 0, 255, valueHchange)

cv2.waitKey(0)                           ## Wait for keystroke
cv2.destroyAllWindows()                  ## Destroy all originals
