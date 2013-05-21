import cv2
import numpy as np
import math

def onChange(x):
	print "in onChange function with argument:", x

cv2.namedWindow('window', cv2.CV_WINDOW_AUTOSIZE)
cv2.createTrackbar("foo", "window", 0, 255, onChange)

cv2.waitKey(0)
cv2.destroyAllWindows()
