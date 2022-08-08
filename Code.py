import copy
import numpy as np
import cv2
from scipy.spatial import distance
# Converting the image to grayscale
image = cv2.imread("1ffa952f-8d87-11e8-9daf-6045cb817f5b..JPG")
cv2.imshow("Original Image", image)
#image = cv2.resize(image, (0, 0), fx=0.2, fy=0.2)
orig = copy.deepcopy(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#----------------without pre-preocessing---------------#
# the area of the image with the largest intensity value
# (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
#
# cv2.circle(image, maxLoc, 5, (255, 0, 0), 2)
#
# # display the results of the naive attempt
# cv2.imshow("Brightest Pixel(without Gaussian blur)", image)
#-------------------------------------------------------#
#----------------with pre-preocessing---------------#
# Gaussian blur to the image
gray = cv2.GaussianBlur(gray, (21, 21), 0)
# searching the brightest-region
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = copy.deepcopy(orig)
cv2.circle(image, maxLoc, 21, (255, 0, 0), 2)
#-------------------------------------------------------#
givenLoc=(2523, 1246)
# Error-Detection using Euclidean Distance
print("Brightest region location from Algorithm: ",maxLoc)
print("Brightest region location from Given: ", givenLoc)
print("Brightest region intensity from Algorithm: ",maxVal)
error=distance.euclidean(givenLoc,maxLoc)
print("Error using Euclidean Distance: ",error)
# display the results with optic disk
cv2.imshow("Detected Optic Disk", image)
cv2.waitKey(0)
