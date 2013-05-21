import cv2
import numpy as np
#import sys
#import cv
#import cv2

def on_track(self):
#	print "TRACKING"
	
	print cv.GetTrackbarPos("Channel", "window")
	cv.Threshold(gray,out, cv.GetTrackbarPos("Channel", "window"),cv.GetTrackbarPos("Channel2", "window"), cv.CV_THRESH_BINARY)
	cv.ShowImage('window',out)
	return

def on_contour(self):
	print "CONTOUR"
#	cv.Threshold(gray, out, 100, 255, cv.CV_THRESH_BINARY)
#	contours,hierarchy=cv.FindContours(out,cv.CV_RETR_LIST,cv.CV_CHAIN_APPROX_SIMPLE)
	return

im = cv2.imread("Plant.jpg")
print "im=",[im]
#gray = cv2.CreateImage(cv2.GetSize(im), 8, 1)
#out = cv2.CreateImage(cv2.GetSize(im),8,1)
cv2.namedWindow('window', cv2.CV_WINDOW_AUTOSIZE)
#cv2.ShowImage('window',im)
#cv.WaitKey(3000)
#cv.Smooth(im, out, cv.CV_GAUSSIAN,7,7)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
out = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)[1]
contours,hierarchy = cv2.findContours(out,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1]
mask = np.zeros(out.shape, np.uint8)
cv2.drawContours(mask,[contours[142]],-1,(100),-1)
i = 0
for contour in contours:
	if len(contour) > 100:
		print i,"=",len(contour)
	i += 1
print contours[1]

cv2.imshow('window', mask)
#cv.WaitKey(3000)
#print type(im)
#cv.SaveImage("foo.png", out)
#cv.CreateTrackbar("Channel", "window", 0, 255, on_track)
#cv.CreateTrackbar("Channel2", "window", 0, 255, on_track)
#cv.CreateTrackbar("Contours", "window", 0, 255, on_contour)
#on_track()
print mask.shape
print mask.shape[0],mask.shape[1]
#mat = cv2.fromarray(mask)
#print "getDims(mat)=",cv2.getDims(mat)
#for x,y in mat
#	if x or y > 0
#		print x,y
#print mask[0], mask[1]
yVals = []
for y in range(mask.shape[1]):
	for x in range(mask.shape[0]):
		if mask[x][y] != 0:
			yVals.append(y)
			break
yVals.sort()
print "yHigh =",yVals[-1],"; yLow =",yVals[0]
#print 'column' in locals()
#print 'column' in globals()
#contours = cv2.findContours(out, cv.CV_RETR_LIST, cv.CV_CHAIN_APPROX_SIMPLE)

cv2.waitKey(0)
