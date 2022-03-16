import cv2
import numpy as np

img = cv2.imread("test-resources\street.jpg")

imgGray = cv2.cvtColor((img), cv2.COLOR_BGR2GRAY) # Black and white image conversion (img, color)
# Obs.: Its BGR not RGB, so it's the inverted version

imgBlur = cv2.GaussianBlur(img, (11,11), 0) # Blur ("borrar") conversion, (img, (odd numbers "how much blur will be used"), 0)

imgCanny = cv2.Canny(img, 500, 400) # Border analize
"""
src: Image
threshold1: It is the High threshold value of intensity gradient.
threshold2: It is the Low threshold value of intensity gradient.
"""

imgDialation = cv2.dilate(imgCanny, np.ones((5,5), np.uint8), iterations=1) # (Border image, matrix/kernel, iteration=thikness)
"""
np.ones((width, height), type) - Creates a matrix with only ones
type - the type of numbers (np.uint8 is the 8-bit or can be called 256 levels, 2 elevated to 8)
"""

imgEroded = cv2.erode(imgDialation, np.ones((5,5), np.uint8), iterations=1) # Opposite of the above one

cv2.imshow("Original Window", img)
cv2.imshow("Gray Window", imgGray)
cv2.imshow("Blur Window", imgBlur)
cv2.imshow("Canny Window", imgCanny)
cv2.imshow("Dialation Window", imgDialation)
cv2.imshow("Eroded Window", imgEroded)

cv2.waitKey(0)