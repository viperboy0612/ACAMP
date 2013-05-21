import cv2
import sys
import numpy as np

img = cv2.imread("../Images/Plant.jpg",cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file
cv2.namedWindow('Display Window')        ## create window for display
cv2.imshow('Display Window',img)         ## Show image in the window
print "size of image: ",img.shape        ## print size of image
cv2.waitKey(0)                           ## Wait for keystroke
cv2.destroyAllWindows()                  ## Destroy all windows
