#Press a key to store a new image for other programs to use
#Programs that use this Tool
# RGBThresholds.py
millis = 10
import cv2
camera_port = 0
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
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
while (True):
	camera_capture = get_image()
	cv2.imshow('window', camera_capture)
	key = cv2.waitKey(millis)
	if key != -1:
		cv2.imwrite("../Images/Webcam.png", camera_capture)
		break
del(camera)
cv2.destroyAllWindows()
