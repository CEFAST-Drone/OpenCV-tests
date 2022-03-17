import cv2
import numpy as np

""" 
# Learning
img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0,0), (255,255), (255, 102, 255), 5) # Creates a line - (image, (start point), (end point), (BGR), thickness), but remembering (x, y)
cv2.rectangle(img, (0,0), (512, 512), (204, 255, 204), 5) # Creates a rectangle
# Obs.: in thickness you can fill all the area of the rectangle, using cv2.FILLED
cv2.circle(img, (255, 255), 100, (153, 255, 255), 5) # Creates a circle - (image, (center point), radious, BGR, thickness)
cv2.putText(img, "Hello World", (200, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2) # Text - (img, text, origin point, font, fontScale, color, thickness)
"""

# Basic Project - Drone Logo
img = np.ones((512, 512, 3), np.uint8)
img[:] = 255,255,255 # White

# Purple Circles
cv2.circle(img, (128,128), 50, (102, 0, 102), 5)
cv2.circle(img, (384,128), 50, (102, 0, 102), 5)
cv2.circle(img, (128,384), 50, (102, 0, 102), 5)
cv2.circle(img, (384,384), 50, (102, 0, 102), 5)
# Black blue circles
cv2.circle(img, (128,128), 30, (102, 51, 0), cv2.FILLED)
cv2.circle(img, (384,128), 30, (102, 51, 0), cv2.FILLED)
cv2.circle(img, (128,384), 30, (102, 51, 0), cv2.FILLED)
cv2.circle(img, (384,384), 30, (102, 51, 0), cv2.FILLED)
# Lines to the center
cv2.line(img, (128,128), (256,256), (102,51,0), 30)
cv2.line(img, (384,128), (256,256), (102,51,0), 30)
cv2.line(img, (128,384), (256,256), (102,51,0), 30)
cv2.line(img, (384,384), (256,256), (102,51,0), 30)
# Central Rectangle
cv2.rectangle(img, (176,176), (336, 336), (102,51,0), cv2.FILLED)
# Text
cv2.putText(img, "CEFAST DRONE", (160, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (102, 51, 0), 1)

cv2.imshow("Image created", img)
cv2.imwrite("./test-resources/chapter 4 Photo.png", img) # Save the photo

cv2.waitKey(0)