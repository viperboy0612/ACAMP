#Store Images Every X Milliseconds
millis = 500

import cv2
 
# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
 temp = get_image()
print("Taking image...")
cv2.namedWindow('window',cv2.CV_WINDOW_AUTOSIZE)
# Take the actual image we want to keep
n = 0
sn = ""
while (True):
	camera_capture = get_image()
	cv2.imshow('window', camera_capture)
	key = cv2.waitKey(millis)
	if (len(str(n)) == 1):
		sn = "00" + str(n)
	elif (len(str(n)) == 2):
		sn = "0" + str(n)
	elif(len(str(n)) == 3):
		sn = str(n)
	else:
		print "ERROR!  Len(n) is not 1-3"
	cv2.imwrite("StoredImages/WebcamImage"+sn+".png", camera_capture)
	n += 1
	if key != -1:
		break
del(camera)
cv2.destroyAllWindows()
