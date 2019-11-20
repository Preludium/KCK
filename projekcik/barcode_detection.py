import numpy as np
import cv2
import imutils
import os
 
def detect(image):
	# to grayscale
	grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
 
	# Scharr gradient
	ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
	# calculate the derivatives from an image
	# max of derivative is the jump of high gradient change 
	gradientX = cv2.Sobel(grayScale, ddepth=ddepth, dx=1, dy=0, ksize=-1)
	gradientY = cv2.Sobel(grayScale, ddepth=ddepth, dx=0, dy=1, ksize=-1)
 
	# subtraction y-gradient & x-gradient
	gradientSub = cv2.subtract(gradientX, gradientY)
	# convert to absolute
	gradient = cv2.convertScaleAbs(gradientSub) 

 
	# blur & threshold
	blurred = cv2.blur(gradient, (9, 9))
	_, thresh = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY) # to binary
 
	# looking for rectangular area to apply morphological operations
	rectSearch = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7)) # specify rect search
	region = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, rectSearch)
 
	# erosion and dilation for better contours searching
	eroded = cv2.erode(region, None, iterations=4)
	erodedDilated = cv2.dilate(eroded, None, iterations=15)
	contours = cv2.findContours(erodedDilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	finalContours = imutils.grab_contours(contours)
 
	if len(finalContours) == 0:
		return None
 
	# get largest bounding box
	c = sorted(finalContours, key=cv2.contourArea, reverse=True)[0]
	rectangle = cv2.minAreaRect(c)
	box = cv2.cv.BoxPoints(rectangle) if imutils.is_cv2() else cv2.boxPoints(rectangle)
	box = np.int0(box)
 
	# return barcode box
	return box 


if __name__ == "__main__":
	# img = cv2.imread(str(os.getcwd()) + '\\fotki\\tel3.jpg')
	# img.resize()
	cap = cv2.VideoCapture(0)
	cap.set(3, 1280)
	cap.set(4, 720)
	while True:
		ret, img = cap.read()
		box = detect(img)
		# if box is not None:
			# cv2.drawContours(img, [box], -1, (0, 255, 0), 2)
		cv2.imshow("Image", box)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
