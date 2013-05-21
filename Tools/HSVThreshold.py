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
	print "satLchange"
def saturationHchange(value):
	print "satHchange"
def valueLchange(value):
	print "valueLchange"
def valueHchange(value):
	print "valueHchange"

def updateImage():
	print "Updating Image"
        COLOR_MIN = np.array([hueL, satL, valL], np.uint8)
        COLOR_MAX = np.array([hueH, 255, 255], np.uint8)
        filtered_hsv = cv2.inRange(img, COLOR_MIN, COLOR_MAX)
        cv2.imshow('hsv', filtered_hsv)

img = cv2.imread("../Images/WebcamImage100.png",cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file
cv2.namedWindow('original')        ## create original for display
cv2.namedWindow('originalhsv')
cv2.namedWindow('hsv')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('original',img)         ## Show image in the original
cv2.imshow('hsv', hsv)
cv2.imshow('originalhsv', hsv)
cv2.createTrackbar("Hue Low", "original", 0, 179, hueLchange)
cv2.createTrackbar("Hue High", "original", 0, 179, hueHchange)

cv2.createTrackbar("Saturation Low", "original", 0, 255, saturationLchange)
cv2.createTrackbar("Saturation High", "original", 0, 255, saturationHchange)

cv2.createTrackbar("Value Low", "original", 0, 255, valueLchange)
cv2.createTrackbar("Value High", "original", 0, 255, valueHchange)

cv2.waitKey(0)                           ## Wait for keystroke
cv2.destroyAllWindows()                  ## Destroy all originals
