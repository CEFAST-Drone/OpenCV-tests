import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) # Creates a matrix, 64, 64 all black (0) ", 3" to be BGR, not RGB
print(img.shape)

img[:] = 255, 0, 0 # Colouring the full image
img[250:262, 250:262] = 0, 255, 0 # Colouring just a part of the image

cv2.imshow("Image created", img)

cv2.waitKey(0)