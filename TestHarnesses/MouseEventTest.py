import cv2
import sys
import numpy as np

#http://opencv-srf.blogspot.com/2011/11/mouse-events.html
#Refer to URL above for all the arguments
def on_mouse(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print "LBUTTONDOWN Position[x,y]: [",x,",", y, "]"

cv2.namedWindow('window', cv2.CV_WINDOW_AUTOSIZE)
im = cv2.imread("../Images/Plant.jpg")
cv2.imshow("window", im) 
cv2.setMouseCallback("window", on_mouse)
cv2.waitKey(0)                           ## Wait for keystroke
cv2.destroyAllWindows()                  ## Destroy all windows


