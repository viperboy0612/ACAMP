import cv2
import sys
import numpy as np

whiteThreshold = 100

def on_mouse(event, x, y, flags, param):
	global img
	if event == cv2.EVENT_LBUTTONDOWN:
		#print "In on_mouse function"
		print "x:",x, ";y:", y
		print [img[y,x]]
		
def whiteFilter(im):
#	if(im[0,0,0]>0):
#		print "WORKS"
	for row in range(480):
		for col in range(640):
			if im[row,col,0] > whiteThreshold and im[row,col,1] > whiteThreshold and im[row,col,2] > whiteThreshold:
				for i in range(3):
					im[row,col,i] = 0	
	return im 

img = cv2.imread("Plant.jpg",cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file

cv2.namedWindow('Display Window')        ## create window for display
new = whiteFilter(img)
cv2.imshow('Display Window',new)         ## Show image in the window
print "size of image: ",img.shape        ## print size of image
cv2.setMouseCallback("Display Window", on_mouse)
cv2.waitKey(0)                           ## Wait for keystroke
cv2.destroyAllWindows()                  ## Destroy all windows
