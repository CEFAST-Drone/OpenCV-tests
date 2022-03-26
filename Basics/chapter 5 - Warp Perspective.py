import cv2
import numpy as np

img = cv2.imread("test-resources\street.jpg")

# Letting the "levis" advertise plan and easy to read
width, height = 200, 200 # sizes of the outdoor
point1 = np.float32([[61,0],[100,22],[61,95],[100,108]]) # Position of the outdoor (the 4 points of it), (x, y), (x+width, y) ...
point2 = np.float32([[0,0],[width, 0],[0, height],[width, height]]) # New sizes
matrix = cv2.getPerspectiveTransform(point1, point2) # Make it plan

imgOutput = cv2.warpPerspective(img, matrix, (width, height)) # Turn it into an image

cv2.imshow("Original Image", img)
cv2.imshow("Levis outdoor", imgOutput)

cv2.waitKey(0)