import cv2
import sys
import numpy as np

img = cv2.imread("../Images/WebcamImage100.png",cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file
cv2.namedWindow('window')        ## create window for display
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('window',hsv)         ## Show image in the window
print "size of image: ",hsv.shape        ## print size of image
cv2.waitKey(0)                           ## Wait for keystroke
cv2.destroyAllWindows()                  ## Destroy all windows
