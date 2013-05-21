import cv2
import sys
import numpy as np

if len(sys.argv)!=2:                  ## Check for error in usage syntax
	print "Too Many Arguments"
else:
	argument = sys.argv[1]  ## Read image file

if (argument == None):                      ## Check for invalid input
	print "Doing Nothing"
else:
	print "argument:", argument        ## print size of image
cv2.waitKey(0)                           ## Wait for keystroke
