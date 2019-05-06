"""
Doc Scanner Script

Function:
		Takes an image, searches for contours
		that represent the "paper" in which our
		table should be in, crops it.
		The script also applies adaptive binarization
		and thresholding to get the black and white
		clean effect for a document.
"""

import cv2
import imutils
import os
from transform import four_point_transform


def scan_img(img_path):
	# load the image and compute the ratio of the old height
	# to the new height, clone it, and resize it
	image = cv2.imread(img_path)
	ratio = image.shape[0] / 500.0
	orig = image.copy()
	image = imutils.resize(image, height = 500)

	# convert the image to grayscale, blur it, and find edges
	# in the image
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 75, 200)

	# find the contours in the edged image, keeping only the
	# largest ones, and initialize the screen contour
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

	# loop over the contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)

		# if our approximated contour has four points, then we
		# can assume that we have found our screen
		if len(approx) == 4:
			screenCnt = approx
			break

	# apply the four point transform to obtain a top-down
	# view of the original image
	warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

	# Thresholding the image to give it the document scanned effect
	warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
	thresholded = cv2.adaptiveThreshold(warped,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,41,13)

	# Writing the output to a file
	# Checks if a file with the same name exists first to avoid overwriting.
	i = 0
	while True:
		exists = os.path.isfile('resources/scan_output/scanned_img' + '_' + str(i) + '.jpg')
		if exists:
			i += 1
			continue
		else:
			cv2.imwrite('resources/scan_output/scanned_img'+ '_' + str(i) + '.jpg', imutils.resize(thresholded, height=2000))
			return thresholded


if __name__ == '__main__':
	scan_img('resources/input/test_img.jpg')
