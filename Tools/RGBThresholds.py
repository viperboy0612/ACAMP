#set argument to camera to use webcam image.  update image with TOOL TakeWebcamImage.py
#To use webcam, run command: python RGBThresholds.py camera
#Otherwise, it will use the default plant image

import cv2
import sys
import numpy as np
import math

redL, redH, greenL, greenH, blueL, blueH= 0,0,0,0,0,0

def redLchange(value):
	global redL
	redL = value
	if redL > redH:
		print "Invalid Value: redL > redH"
	else:
		updateImage()
	
def redHchange(value):
	global redH
	redH = value
	if redH < redL:
		print "Invalid Value: redH > redL"
	else:
		updateImage()

def greenLchange(value):
	global greenL
	greenL = value
	if greenL > greenH:
		print "Invalid Value: greenL > greenH"
	else:
		updateImage()

def greenHchange(value):
	global greenH
	greenH = value
	if greenH < greenL:
		print "Invalid Value: greenH < greenL"
	else:
		updateImage()

def blueLchange(value):
	global blueL
	blueL = value
	if blueL > blueH:
		print "Invalid Value: blueL > blueH"
	else:
		updateImage()

def blueHchange(value):
	global blueH
	blueH = value
	if blueH < blueL:
		print "Invalid Value: blueH > blueL"
	else:
		updateImage()

def updateImage():
	print "Updating Image"
	COLOR_MIN = np.array([redL, blueL, greenL], np.uint8)
	COLOR_MAX = np.array([redH, blueH, greenH], np.uint8)
	no_white = cv2.inRange(im, COLOR_MIN, COLOR_MAX)
	cv2.imshow('window', no_white)

if len(sys.argv) == 2 and sys.argv[1] == 'camera':
	print len(sys.argv),sys.argv[1]
	im = cv2.imread("../Images/Webcam.png")
	print im
	if im == None:
		im = cv2.imread("../Images/Plant.jpg")
else:
	im = cv2.imread("../Images/Plant.jpg")
cv2.namedWindow('original', cv2.CV_WINDOW_AUTOSIZE)
cv2.imshow('original', im)
cv2.namedWindow('window', cv2.CV_WINDOW_AUTOSIZE)

cv2.createTrackbar("Red Low", "window", 0, 255, redLchange)
cv2.createTrackbar("Red High", "window", 0, 255, redHchange)

cv2.createTrackbar("Green Low", "window", 0, 255, greenLchange)
cv2.createTrackbar("Green High", "window", 0, 255, greenHchange)

cv2.createTrackbar("Blue Low", "window", 0, 255, blueLchange)
cv2.createTrackbar("Blue High", "window", 0, 255, blueHchange)

cv2.imshow('window', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
