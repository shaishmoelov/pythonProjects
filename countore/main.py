#conversion to grayscale
#Blurring to reduce high frequency noise to make our contour detection process more accurate.
#Binarization of the image. Typically edge detection and thresholding are used for this process. In this post, we’ll be applying thresholding.
import imutils
import argparse

import cv2

# Load the image and convert it to grayscale
image = cv2.imread("out1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

# Find the contours in the binary image
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)

# Select the contour that represents the cross
for contour in contours:

	# # Check if the contour has four vertices
	# if len(contour) != 4:
	# 	continue

	# Calculate the moments of the contour
	M = cv2.moments(contour)

	# Calculate the center of the contour
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	# Draw the center of the contour on the image
	cv2.circle(image, (cX, cY), 5, (255, 0, 0), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Show the image
cv2.imshow("Image", image)
cv2.waitKey(0)
#
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the input image")
# args = vars(ap.parse_args())
#
# # load the image, convert it to grayscale, blur it slightly,
# # and threshold it
# image = cv2.imread(args["image"])
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#
# # find contours in the thresholded image
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
#
# # loop over the contours
# for c in cnts:
# 	# compute the center of the contour
# 	M = cv2.moments(c)
# 	cX = int(M["m10"] / M["m00"])
# 	cY = int(M["m01"] / M["m00"])
# 	# draw the contour and center of the shape on the image
# 	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
# 	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
# 	cv2.putText(image, "center", (cX - 20, cY - 20),
# 		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
# 	# show the image
# 	cv2.imshow("Image", image)
# 	cv2.waitKey(0)