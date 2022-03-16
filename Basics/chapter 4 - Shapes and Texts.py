import cv2
import numpy as np

# 37:50 of the video
img = np.zeros((512, 512, 3), np.uint8) # Creates a matrix, 64, 64 all black (0) ", 3" to be BGR, not RGB


cv2.imshow("Image created", img)

cv2.waitKey(0)